import numpy as np
import cv2

def nothing(x):
    print(x)


img=np.zeros((300,512,3),np.uint8)
cv2.namedWindow('Frame')

cv2.createTrackbar('B', 'Frame', 0, 255, nothing)
cv2.createTrackbar('G', 'Frame', 0, 255, nothing)
cv2.createTrackbar('R', 'Frame', 0, 255, nothing)

while(1):
    cv2.imshow('Frame',img)
    k=cv2.waitKey(1) & 0xFF
    if k==27:
        break

    b = cv2.getTrackbarPos('B','Frame')
    g = cv2.getTrackbarPos('G', 'Frame')
    r = cv2.getTrackbarPos('R', 'Frame')

    img[:]=[b,g,r]

cv2.destroyAllWindows()