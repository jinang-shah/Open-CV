import numpy as np
import cv2 as cv

img=cv.imread('sudoku.png')
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, thr1=cv.threshold(img,127,255,cv.THRESH_BINARY,255)
thr2=cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
thr3=cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

cv.imshow('IMAGE',img)
cv.imshow('Simple THRESHOLD',thr1)
cv.imshow('Adaptive THRESHOLD',thr2)
cv.imshow('2-Adaptive THRESHOLD ',thr3)

cv.waitKey(0)
cv.destroyAllWindows()
