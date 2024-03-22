import cv2 as cv
import sys, os

from windowCapture import WindowCapture
from vision import findObjectPosition
import keyboard
import time
import pyautogui
import numpy as np

os.chdir(os.path.dirname(os.path.abspath(__file__)))

wincap = WindowCapture()

loop_time = time.time()
while(True):
    screenshot = wincap.get_screenshot()
    # screenshot = pyautogui.screenshot(region=(20, 20, 80, 80))
    # screenshot = np.array(screenshot)
    # cv.imshow('Computer Vision', screenshot)
    waitFishing = findObjectPosition('./img/waitFishing.png',screenshot,0.99, True,None)
    if waitFishing == True:
        keyboard.press_and_release('f')
        time.sleep(200/1000)
    # refresh = findObjectPosition('./img/refresh.png',screenshot,0.90, True,None)
    # if refresh == True:
    #     keyboard.press_and_release('f')
    #     time.sleep(30)
    

        
    print('FPS {}'.format(1 / (time.time() -loop_time)))
    loop_time = time.time()
    if(cv.waitKey(1) == ord('q')):
        cv.destroyAllWindows()
        break

# window_capture()
print('done')