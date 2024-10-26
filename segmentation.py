import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

cam  = cv.VideoCapture(0)

while True:
        ret, frame = cam.read()
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        
        upper_color = np.array([138,255,255])
        lower_color = np.array([78,158,124])
        
        mask = cv.inRange(hsv, lower_color, upper_color)
        
        cv.imshow("camera",frame)
        cv.imshow("mask", mask)
        
        if cv.waitKey(1)==ord('q'):
                break

cv.destroyAllWindows()
        

