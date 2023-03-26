import cv2 as cv
import numpy as np
from time import time
from windowcapture import WindowCapture

winCap = WindowCapture("Osu!")

loop_time: float
loop_time = time()
while True:

    screenShot = winCap.getScreenShot()
    
    

    cv.imshow('Computer Vision', screenShot)

    #loop rate 
    print('FPS {}'.format(1/(time() - loop_time)))
    loop_time = time()

    if cv.waitKey(33) & 0xFF in (ord('q'),27,):
        break