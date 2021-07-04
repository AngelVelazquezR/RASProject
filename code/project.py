# import required libraries
import numpy as np
import matplotlib.pyplot as plt
import cv2
import math

img_name = '../img/highway.mp4'

cap = cv2.VideoCapture(img_name)


while(cap.isOpened()):

    ret, frame = cap.read()


    ##TO-DO Gray scale
    grey = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    ##TO-DO Gaussian Blur
    kernel_size = (11,11)
    blur_grey = cv2.GaussianBlur(grey, kernel_size, 0)
    for i in range(5):
        blur_grey = cv2.GaussianBlur(blur_grey, kernel_size, 0)

    ##TO-DO Canny
    low_threshold = 5
    high_threshold = 12
    edges = cv2.Canny(blur_grey, low_threshold, high_threshold, apertureSize=3)

    ##TO-DO ROI (Region Of Interest)

    ##TO-DO HOUGHT LINES

            
            
    cv2.namedWindow('Video', cv2.WINDOW_NORMAL)
    cv2.imshow('Video', frame)
    cv2.resizeWindow('Video', 800,500)
    
    cv2.namedWindow('Gaus', cv2.WINDOW_NORMAL)
    cv2.imshow('Gaus', blur_grey)
    cv2.resizeWindow('Gaus', 800,500)

    cv2.namedWindow('Canny', cv2.WINDOW_NORMAL)
    cv2.imshow('Canny', edges)
    cv2.resizeWindow('Canny', 800,500)
 

    # Press Q on keyboard to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()
        

