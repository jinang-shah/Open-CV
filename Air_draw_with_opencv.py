import numpy as np
import cv2 as cv
from collections import deque
from playsound import playsound


def nothing(x):
    pass

cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 2200)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 2000)

canvas = np.ones((2000, 2000), np.uint8)

cv.namedWindow('Tracking')
cv.createTrackbar('LH', 'Tracking',98, 255,nothing)
cv.createTrackbar('LS', 'Tracking',151, 255,nothing)
cv.createTrackbar('LV', 'Tracking',121, 255,nothing)
cv.createTrackbar('UH', 'Tracking',176, 255,nothing)
cv.createTrackbar('US', 'Tracking',255, 255,nothing)
cv.createTrackbar('UV', 'Tracking',255, 255,nothing)

yellow_list = [deque(maxlen=1024)]
blue_list = [deque(maxlen=1024)]
red_list = [deque(maxlen=1024)]
green_list = [deque(maxlen=1024)]

blue_index = 0
yellow_index = 0
red_index = 0
green_index = 0

blue = (255, 255, 0)
yellow = (0,255,255)
red = (0, 0, 255)
green = (0, 255, 0)

colors = [yellow, blue, red, green]
marker_color = 0

kernal = np.ones((5,5),np.uint8)

while True:
  _,frame = cap.read()

  cv.rectangle(frame, (20,5), (100,50), yellow, 2)
  cv.rectangle(frame, (140, 5), (220, 50), blue, 2)
  cv.rectangle(frame, (260, 5), (340, 50), red, 2)
  cv.rectangle(frame, (380, 5), (460, 50), green, 2)


  hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

  # setting upper and lower HSV values based on the object color
  l_h = cv.getTrackbarPos('LH', 'Tracking')
  l_s = cv.getTrackbarPos('LS', 'Tracking')
  l_v = cv.getTrackbarPos('LV', 'Tracking')

  u_h = cv.getTrackbarPos('UH', 'Tracking')
  u_s = cv.getTrackbarPos('US', 'Tracking')
  u_v = cv.getTrackbarPos('UV', 'Tracking')

  lower = np.array([l_h, l_s, l_v])
  upper = np.array([u_h, u_s, u_v])

  mask1 = cv.inRange(hsv, lower, upper)
  mask = cv.erode(mask1, kernal, iterations=1)
  mask = cv.morphologyEx(mask, cv.MORPH_OPEN, kernal)
  mask = cv.dilate(mask, kernal, iterations=1)

  contours ,hirarchy = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
  center = None

  if len(contours)>0:
      ((x,y),radius) = cv.minEnclosingCircle(contours[0])
      cv.circle(frame, (int(x), int(y)), 10, (0, 255, 255), 3)
      cv.circle(canvas, (int(x), int(y)), 10, (0, 255, 255), 3)
      center = (int(x), int(y))
      if center[1]<=50 :
        if center[0] >= 20 and center[0] <= 100:
          playsound('drum sound/Bass-Drum-Hit.mp3')
          marker_color = 0  #yellow
        elif center[0] >= 140 and center[0] <= 220:
          playsound('drum sound/Bass-Drum-Hit.mp3')
          marker_color = 1  #blue
        elif center[0] >= 280 and center[0] <= 360:
          playsound('drum sound/Floor-Tom-Drum-Hit.mp3')
          marker_color = 2  #red
        elif center[0] >= 400 and center[0] <= 480:
          playsound('drum sound/Snare-Drum-Hit.mp3')
          marker_color = 3  #green
      else:
        if marker_color == 0:
          yellow_list[yellow_index].appendleft(center)
        elif marker_color == 1:
          blue_list[blue_index].appendleft(center)
        elif marker_color == 2:
          red_list[red_index].appendleft(center)
        elif marker_color == 3:
          green_list[green_index].appendleft(center)

  else:
    yellow_list.append(deque(maxlen=512))
    yellow_index += 1
    blue_list.append(deque(maxlen=512))
    blue_index += 1
    red_list.append(deque(maxlen=512))
    red_index += 1
    green_list.append(deque(maxlen=512))
    green_index += 1


  for i in range(len(yellow_list)):
    for j in range(len(yellow_list[i])):
      if yellow_list[i][j] is not None or yellow_list[i][j+1] is not None:
        continue
      cv.line(frame, yellow_list[i][j], yellow_list[i][j+1], yellow, 3)
      cv.line(canvas, yellow_list[i][j], yellow_list[i][j + 1], yellow, 3)

  """
  color_points = [blue_list, yellow_list, red_list, green_list]
  
  for i in range(len(color_points)):
    for j in range(len(color_points[i])):
      for k in range( len(color_points[i][j])-1):
        if color_points[i][j][k] is not None or color_points[i][j][k+1] is not  None:
          continue
        cv.line(frame, color_points[i][j][k], color_points[i][j][k+1], colors[i], 3)
  """

  #for point in red_list:
   #cv.circle(frame, point, 6, red, -1)
  #for point in green_list:
    #cv.circle(frame, point, 6, green, -1)
  #cv.circle(canvas, point, 3, (0, 0, 255),-1)


  canvas = cv.flip(canvas, 1)
  frame = cv.flip(frame, 1)

  #outtput
  cv.imshow('Frame', frame)
  #cv.imshow('Threshold',mask)
  #cv.imshow('Canvas', canvas)

  if cv.waitKey(1) & 0xFF == ord('q'):
      break

cap.release()
cv.destroyAllWindows()