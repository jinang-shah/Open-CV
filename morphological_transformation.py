import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img=cv.imread('color_balls.jpg',cv.IMREAD_GRAYSCALE)
_, mask = cv.threshold(img,220,255,cv.THRESH_BINARY_INV)
kernal=np.ones((2,2),np.uint8)
dilation=cv.dilate(mask,kernal,iterations=5)
erosion= cv.erode(mask,kernal,iterations=1)

cv.imshow('IMAGE',img)
cv.imshow('MASK',mask)
cv.imshow('DILATION',dilation)
cv.imshow('EROSION',erosion)

cv.waitKey(0)
cv.destroyAllWindows()



""""
titles=['image','mask']
images=[img,mask]

for i in range(2):
    plt.subplots(1,2,sharex=False,sharey=False ),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

"""
