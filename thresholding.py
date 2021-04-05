import numpy as np
import cv2
import matplotlib.pyplot as plt

img=cv2.imread('black_and_white_gradient.jpg',0)
_,thr1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
_,thr2=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
_,thr3=cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
_,thr4=cv2.threshold(img,127,255,cv2.THRESH_MASK)
_,thr5=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
_,thr6=cv2.threshold(img,127,255,cv2.THRESH_OTSU)

titles=['IMAGE','BINARY', 'BINARY INV', 'TRUNC', 'MASK', ' TOZERO', 'OTSU']
images=[img,thr1,thr2,thr3,thr4,thr5,thr6]
for i in range(6):
    plt.subplots(2, 3, i+1), plt.imshow(images[i],'gray')

    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
    plt.show()
#cv2.imshow('IMAGE',img)
#cv2.imshow('THRESHOLD 1',thr1)
#cv2.imshow('THRESHOLD 2',thr2)
#cv2.imshow('THRESHOLD 3',thr3)
#cv2.imshow('THRESHOLD 4',thr4)
#cv2.imshow('THRESHOLD 5',thr5)
#cv2.imshow('THRESHOLD 6',thr6)


cv2.waitKey(0)
cv2.destroyAllWindows()