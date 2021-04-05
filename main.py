import cv2 as cv
import numpy as np

#img=cv.imread('jinang.jpg', -1)
img=np.zeros([1080,1080,3],np.uint8)
print(img.shape)

cv.line(img, (0, 0), (255, 255), (255,0 , 255), 3)
cv.arrowedLine(img, (10, 10), (200, 200), (255,0,0), (5))
cv.rectangle(img, (200, 200),(350, 350), (0 ,0 , 255), -1)
cv.circle(img,(400, 400), 100, (0, 0, 255), -1)
font=cv.FONT_HERSHEY_DUPLEX
cv.putText(img, 'Jinang Shah', (200,80), font, 4, (0,100,255), 5)

cv.imshow('My Image' ,img)
k=cv.waitKey(0)
if(k==27):
   cv.destroyAllWindows()
elif(k==ord('s')):
   cv.imwrite('jinang_copy.jpg',img)