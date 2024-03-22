import cv2 as cv
import numpy as np


def findObjectPosition(object_img_path, scan_img, threshold=0.59,gray=None ,debug_mode=None):
    if gray == True:
        object_img = cv.imread(object_img_path,cv.IMREAD_GRAYSCALE)
        scan_img = cv.cvtColor(scan_img, cv.COLOR_BGR2GRAY)
    else:
        object_img = cv.imread(object_img_path,cv.IMREAD_UNCHANGED)
    result = cv.matchTemplate(scan_img, object_img,cv.TM_CCOEFF_NORMED)
    isFound = False
    # Get the best match position
    min_val, max_val,min_loc, max_loc = cv.minMaxLoc(result)

    # print("Best match top left pos: %s" % str(max_loc))
    print("Best match confidence: %s" % str(max_val))
    if max_val >= threshold:
        # print("Matched found")
        isFound = True

        #get dimensions of the magikarp image
        if debug_mode == 'rect':
            object_img_w = object_img.shape[1]
            object_img_h = object_img.shape[0]

            top_left = max_loc
            bottom_right = (top_left[0] + object_img_w, top_left[1] + object_img_h)

            cv.rectangle(scan_img, top_left, bottom_right, color=(0,255,0), thickness=2, lineType=cv.LINE_4)
            # cv.imshow("Result", scan_img)
            # cv.waitKey()
    if debug_mode:
        cv.imshow("result.png", scan_img)
    return isFound


