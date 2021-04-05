import numpy as np
import cv2

def nothing(x):
    pass

cap= cv2.VideoCapture(0);

cv2.namedWindow('Tracking')
cv2.createTrackbar('LH', 'Tracking',0, 255,nothing)
cv2.createTrackbar('LS', 'Tracking',0, 255,nothing)
cv2.createTrackbar('LV', 'Tracking',0, 255,nothing)
cv2.createTrackbar('UH', 'Tracking',255, 255,nothing)
cv2.createTrackbar('US', 'Tracking',255, 255,nothing)
cv2.createTrackbar('UV', 'Tracking',255, 255,nothing)

while True:
    #frame = cv2.imread('color_balls.jpg')
    _ ,frame=cap.read()

    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos('LH', 'Tracking')
    l_s = cv2.getTrackbarPos('LS', 'Tracking')
    l_v = cv2.getTrackbarPos('LV', 'Tracking')

    u_h = cv2.getTrackbarPos('UH', 'Tracking')
    u_s = cv2.getTrackbarPos('US', 'Tracking')
    u_v = cv2.getTrackbarPos('UV', 'Tracking')

    lower_blue=np.array([l_h,l_s,l_v])
    upper_blue=np.array([u_h,u_s,u_v])

    mask=cv2.inRange(hsv,lower_blue,upper_blue)


    res=cv2.bitwise_and(frame,frame, mask=mask)

    cv2.imshow('IMAGE', frame)
    cv2.imshow('MASK', mask)
    cv2.imshow('BIT AND', res)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
