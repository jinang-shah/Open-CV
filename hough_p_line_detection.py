import numpy as np
import cv2 as cv

img=cv.imread('road4.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
edges=cv.Canny(gray,50,150,apertureSize=3)
cv.imshow('CANNY ADGE DETECTION',edges)

minLineLength = 100
maxLineGap = 10
lines = cv.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
for x1,y1,x2,y2 in lines[0]:
    cv.line(img,(x1,y1),(x2,y2),(0,255,0),2)

cv.imshow('IMAGE',img)

cv.waitKey(0)
cv.destroyAllWindows()