import cv2 as cv
import numpy as np
from time import time
from windowcapture import WindowCapture

winCap = WindowCapture("Osu!")



loop_time: float
loop_time = time()
while True:

    screenShot = winCap.getScreenShot()

    screenShot = cv.cvtColor(screenShot, cv.COLOR_BGR2HSV)
    
    mask = cv.inRange(screenShot, np.array([0,0,128]), np.array([255,255,255]))

    cv.imshow('Computer Vision', mask)

    #loop rate 
    print('FPS {}'.format(1/(time() - loop_time)))
    loop_time = time()

    if cv.waitKey(33) & 0xFF in (ord('q'),27,):
        break