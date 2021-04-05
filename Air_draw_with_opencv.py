import numpy as np
import cv2 as cv

def nothing(x):
    pass

cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 2000)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 2000)



cv.namedWindow('Tracking')
cv.createTrackbar('LH', 'Tracking',98, 255,nothing)
cv.createTrackbar('LS', 'Tracking',151, 255,nothing)
cv.createTrackbar('LV', 'Tracking',121, 255,nothing)
cv.createTrackbar('UH', 'Tracking',176, 255,nothing)
cv.createTrackbar('US', 'Tracking',255, 255,nothing)
cv.createTrackbar('UV', 'Tracking',255, 255,nothing)

yellow = []

while True:
  _,frame = cap.read()

  canvas = np.ones((2000, 2000), np.uint8)

  hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

  l_h = cv.getTrackbarPos('LH', 'Tracking')
  l_s = cv.getTrackbarPos('LS', 'Tracking')
  l_v = cv.getTrackbarPos('LV', 'Tracking')

  u_h = cv.getTrackbarPos('UH', 'Tracking')
  u_s = cv.getTrackbarPos('US', 'Tracking')
  u_v = cv.getTrackbarPos('UV', 'Tracking')

  lower = np.array([l_h, l_s, l_v])
  upper = np.array([u_h, u_s, u_v])

  kernal = np.ones((5,5),np.uint8)

  mask1 = cv.inRange(hsv, lower, upper)
  mask = cv.erode(mask1, kernal, iterations=1)
  mask = cv.morphologyEx(mask, cv.MORPH_OPEN, kernal)
  mask = cv.dilate(mask, kernal, iterations=1)

  contours ,hirarchy = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
  if len(contours)>0:
      ((x,y),radius) = cv.minEnclosingCircle(contours[0])
      cv.circle(frame, (int(x), int(y)), 10, (0, 255, 255), 3)
      yellow.append((int(x), int(y)))

  for point in yellow:
    cv.circle(frame, point, 6, (0,0,255), -1)
    #cv.circle(canvas, point, 3, (0, 0, 255),-1)



  """"
  for contour in contours:

      (x,y),radius = cv.minEnclosingCircle(contour)

      if cv.contourArea(contour) < 500:
          continue
      cv.circle(frame, (int(x),int(y)) , int(radius) , (0,255,0) , 3)

  print(len(contours))
  cv.drawContours(frame, contours, 0, (0,0,255), 2)
  """
  canvas = cv.flip(canvas, 1)
  frame = cv.flip(frame, 1)

  #outtput
  cv.imshow('Frame', frame)
  cv.imshow('Threshold',mask)
  cv.imshow('Canvas', canvas)

  if cv.waitKey(1) & 0xFF == ord('q'):
      break

cap.release()
cv.destroyAllWindows()