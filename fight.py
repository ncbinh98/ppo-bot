import cv2 as cv
import sys, os

from windowCapture import WindowCapture
from vision import findObjectPosition
import keyboard
import time

wincap = WindowCapture()

loop_time = time.time()
while(True):
    screenshot = wincap.get_screenshot()
    # cv.imshow('Computer Vision', screenshot)

    # findPokemon = findObjectPosition('./img/magikarp.png',screenshot,0.95, None,None)
    # findPokemon1 = findObjectPosition('./img/luvdisc.png',screenshot,0.90, True,None)
    fight = findObjectPosition('./img/fight.png',screenshot,0.90, True,None)
    # if fight == True and (findPokemon == True or findPokemon1 == True):
    if fight == True:
        keyboard.press_and_release('1')
        time.sleep(200/1000)
        keyboard.press_and_release('1')

        
    print('FPS {}'.format(1 / (time.time() -loop_time)))
    loop_time = time.time()
    if(cv.waitKey(1) == ord('q')):
        cv.destroyAllWindows()
        break

# window_capture()
print('done')