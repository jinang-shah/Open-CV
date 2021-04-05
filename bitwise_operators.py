import numpy as np
import cv2

img1=np.zeros((250,250,3),np.uint8)
img2=cv2.imread('black_white.jpg')
img2=cv2.resize(img2,(250,250))
cv2.imshow('IMG 1',img1)
cv2.imshow('IMG 2',img2)

bit_NOT=cv2.bitwise_not(img2)
cv2.imshow('BIT NOT',bit_NOT)

bit_or=cv2.bitwise_or(img1,img2)
cv2.imshow('BIT OR',bit_or)

bit_and=cv2.bitwise_and(img2,img1)
cv2.imshow('BIT AND',bit_and)

bit_xor=cv2.bitwise_xor(img2,img1)
cv2.imshow('BIT XOR',bit_xor)

cv2.waitKey(0)
cv2.destroyAllWindows()