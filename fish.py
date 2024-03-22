import cv2 as cv
import sys, os

from windowCapture import WindowCapture
from vision import findObjectPosition
import keyboard
import time

os.chdir(os.path.dirname(os.path.abspath(__file__)))
script_dir = sys.path[0]
img_path = os.path.join(script_dir, '../img/pokemon-img/magikarp.png')
wincap = WindowCapture()

loop_time = time.time()
while(True):
    screenshot = wincap.get_screenshot()
   
    # cv.imshow('Computer Vision', screenshot)
    minigame_fish = findObjectPosition('./img/fish.png',screenshot,0.90, True,None)
    if minigame_fish == True:
        keyboard.press_and_release('space')
        
    print('FPS {}'.format(1 / (time.time() -loop_time)))
    loop_time = time.time()
    if(cv.waitKey(1) == ord('q')):
        cv.destroyAllWindows()
        break

# window_capture()
print('done')