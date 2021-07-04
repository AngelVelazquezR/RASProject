# import required libraries
import matplotlib.pyplot as plt
import cv2

img_name = '../img/highway.mp4'

cap = cv2.VideoCapture(img_name)


if(cap.isOpened()):

    ret, frame = cap.read()
    rgbimage =  cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    plt.imshow(rgbimage)
    plt.show()



