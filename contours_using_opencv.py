import numpy as np
import cv2 as cv

img=cv.imread('shapes.png')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret, thresh=cv.threshold(gray,127,255,0)
contours, hirarchy= cv.findContours(thresh,cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
print('numbers of contours : '+str(len(contours)))
print(contours[0])

cv.drawContours(img,contours, -1, (0, 2550, 250),3)

cv.imshow('IMAGE',img)
cv.imshow('GRAY',gray)

cv.waitKey(0)
cv.destroyAllWindows()