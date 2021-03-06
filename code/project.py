# import required libraries
import numpy as np
import matplotlib.pyplot as plt
import cv2
import math

from numpy.core.numerictypes import maximum_sctype

def regionOfInterest(img, vertices):
    mask = np.copy(img)*0
    cv2.fillPoly(mask, vertices, 255)
    masked_image = cv2.bitwise_and(img,mask)
    return masked_image

img_name = '../img/highway.mp4'

cap = cv2.VideoCapture(img_name)


while(cap.isOpened()):

    ret, frame = cap.read()


    ##TO-DO Gray scale
    grey = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    ##TO-DO Gaussian Blur
    kernel_size = (5,5)
    blur_grey = cv2.GaussianBlur(grey, kernel_size, 0)
    for i in range(5):
        blur_grey = cv2.GaussianBlur(blur_grey, kernel_size, 0)

    ##TO-DO Canny
    low_threshold = 10
    high_threshold = 70
    edges = cv2.Canny(blur_grey, low_threshold, high_threshold, apertureSize=3)

    ##TO-DO ROI (Region Of Interest)
    bottom_left = (300,720)
    bottom_right = (1100,720)
    top_left = (523,444)
    top_right = (720,444)
    vertices = np.array([[bottom_left,top_left,top_right,bottom_right]],dtype=np.int32)
    masked_edges = regionOfInterest(edges,vertices)
    
    ##TO-DO HOUGHT LINES

    rho = 1                  # distance resolution in pixels of the Hough grid
    theta = np.pi/180        # angular resolution in radians of the Hough grid
    threshold = 15           # minimum number of votes (intersections in Hough grid cell)
    min_line_len = 5         # minimum number of pixels making up a line
    max_line_gap = 150       # maximum gap in pixels between connectable line segments


    houghtLines = cv2.HoughLinesP(masked_edges,rho,theta,threshold, np.array([]), minLineLength=min_line_len, maxLineGap=max_line_gap)
    
    """
    for x in range(0,len(houghtLines)):
        for x1,y1,x2,y2 in houghtLines[x]:
            cv2.line(frame,(x1,y1),(x2,y2),(255,0,0),3)
    """        

    if houghtLines is not None:

        left_lineX = []
        left_lineY = []
        right_lineX = []
        right_lineY = []

        for line in houghtLines:
            for x1,y1,x2,y2 in line:
                slope = (y2-y1)/(x2-x1)
                if math.fabs(slope) < 0.4:
                    continue
                if slope <=0 :
                    left_lineX.extend([x1,x2])
                    left_lineY.extend([y1,y2])
                else:
                    right_lineX.extend([x1,x2])
                    right_lineY.extend([y1,y2])

    if len(left_lineX) > 0 and len(left_lineY) > 0 and len(right_lineX) > 0 and len(right_lineY) > 0:

        poly_left = np.poly1d(np.polyfit(left_lineY,left_lineX,deg=1))
        poly_right = np.poly1d(np.polyfit(right_lineY,right_lineX,deg=1))

        maxY = 720
        minY = 400

        leftXstart = int(poly_left(maxY))
        leftXend = int(poly_left(minY))

        rightXstart = int(poly_right(maxY))
        rightXend = int(poly_right(minY))

        defines_lines = [[
            [leftXstart,maxY,leftXend,minY],
            [rightXstart,maxY,rightXend,minY]
        ]]

        for x in range(0,len(defines_lines)):
            for x1,y1,x2,y2 in defines_lines[x]:
                cv2.line(frame,(x1,y1),(x2,y2),(0,0,255),5)


    cv2.namedWindow('Video', cv2.WINDOW_NORMAL)
    cv2.imshow('Video', frame)
    cv2.resizeWindow('Video', 800,500)
    
    #cv2.namedWindow('Gaus', cv2.WINDOW_NORMAL)
    #cv2.imshow('Gaus', blur_grey)
    #cv2.resizeWindow('Gaus', 800,500)

    cv2.namedWindow('Canny', cv2.WINDOW_NORMAL)
    cv2.imshow('Canny', edges)
    cv2.resizeWindow('Canny', 800,500)

    cv2.namedWindow('Masked', cv2.WINDOW_NORMAL)
    cv2.imshow('Masked', masked_edges)
    cv2.resizeWindow('Masked', 800,500)
 

    # Press Q on keyboard to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()
        

