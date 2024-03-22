from mss import mss
import cv2
from PIL import Image
import numpy as np
from time import time

mon = {'top': 400, 'left':500, 'width':580, 'height':500}
sct = mss()

class WindowCapture():
    # w = 0 # set this
    # h = 0 # set this
    # hwnd = None
    # cropped_x = 0
    # cropped_y = 0
    # offset_x = 0
    # offset_y = 0

    # def __init__(self, window_name):
    #     #get the window size

    #     # self.w = 1920
    #     # self.h = 1080

    #     if window_name is None:
    #         self.hwnd = win32gui.GetDesktopWindow()
    #     else:
    #         self.hwnd = win32gui.FindWindow(None, window_name)
    #         if not self.hwnd:
    #             raise Exception('Window not found: {}'.format(window_name))

    #     #get the window size
    #     window_rect = win32gui.GetWindowRect(self.hwnd)
    #     self.w = window_rect[2] - window_rect[0]
    #     self.h = window_rect[3] - window_rect[1]

    #     #Account for the window border and titlebar and cut them off

    #     border_pixels = 100
    #     titlebar_pixels = 350
    #     self.w = self.w - (border_pixels * 2)
    #     self.h = self.h - titlebar_pixels - border_pixels
    #     self.cropped_x = border_pixels
    #     self.cropped_y = titlebar_pixels

    def get_screenshot(self):
        sct_img = sct.grab(mon)
        img = Image.frombytes('RGB', (sct_img.size.width, sct_img.size.height), sct_img.rgb)
        img_bgr = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        img = np.array(img_bgr)
        return img
