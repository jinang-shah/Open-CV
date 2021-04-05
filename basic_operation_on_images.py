import numpy as np
import cv2

img=cv2.imread('football.jpg')
img1=cv2.imread('yash_jinang.jpg')
img2=cv2.imread('yaman.jpg')

print(img.shape)
print(img.size)
print(img.dtype)

b,g,r=cv2.split(img)
cv2.imshow('BLUE',b)
cv2.imshow('GREEN',g)
cv2.imshow('RED',r)

img=cv2.merge((b,g,r))
cv2.imshow('IMAGE',img)


img1=cv2.resize(img1,(512,512,))
img2=cv2.resize(img2,(512,512,))

dst=cv2.addWeighted(img1,0.5,img2,0.3,0)
cv2.imshow('Added Images',dst)

cv2.waitKey(0)
cv2.destroyAllWindows()