import numpy as np
import cv2 as cv
from playsound import playsound
import pygame
import time
from pydub import AudioSegment
from pydub.playback import play

def nothing(x):
    pass


cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 2200)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 2000)

print(cap.get(cv.CAP_PROP_FRAME_WIDTH),cap.get(cv.CAP_PROP_FRAME_HEIGHT))

cv.namedWindow('Tracking')
cv.createTrackbar('LH', 'Tracking', 98, 255, nothing)
cv.createTrackbar('LS', 'Tracking', 151, 255, nothing)
cv.createTrackbar('LV', 'Tracking', 121, 255, nothing)
cv.createTrackbar('UH', 'Tracking', 176, 255, nothing)
cv.createTrackbar('US', 'Tracking', 255, 255, nothing)
cv.createTrackbar('UV', 'Tracking', 255, 255, nothing)

blue = (255, 255, 0)
yellow = (0, 255, 255)
red = (0, 0, 255)
green = (0, 255, 0)
temp = (255,0,255)

color = [blue, yellow, red, green,temp]


kernal = np.ones((5, 5), np.uint8)

while True:
    _, frame = cap.read()
    pygame.init()

    x1 = 60
    x2 = x1 + 200
    y1 = 300
    y2 = 500

    for i in range(5):
        cv.rectangle(frame, (x1, y1), (x2, y2), color[i], 2)
        x1 = x2+40
        x2 = x1+200

    """
    cv.rectangle(frame, (20, 300), (220, 500), yellow, 2)
    cv.rectangle(frame, (240, 300), (440, 500), blue, 2)
    cv.rectangle(frame, (480, 300), (680, 500), red, 2)
    cv.rectangle(frame, (720, 300), (920, 500), green, 2)
    """

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

    contours, hirarchy = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    center = None

    if len(contours) > 0:
        ((x, y), radius) = cv.minEnclosingCircle(contours[0])
        cv.circle(frame, (int(x), int(y)), 10, (0, 255, 255), 3)
        center = (int(x), int(y))
        if 300 <= center[1] <= 500:
            if center[0] >= 60 and center[0] <= 260:
                pygame.mixer.Sound('drum sound/Bass-Drum-Hit.mp3').play()  # playing the .wav file
                time.sleep(0.08)
                pygame.mixer.Sound('drum sound/Bass-Drum-Hit.mp3').stop()

                #playsound('drum sound/Bass-Drum-Hit.mp3')

            elif center[0] >= 300 and center[0] <= 500:
                pygame.mixer.Sound('drum sound/Hi-Hat-Closed-Hit.mp3').play()  # playing the .wav file
                time.sleep(0.08)
                pygame.mixer.Sound('drum sound/Hi-Hat-Closed-Hit.mp3').stop()

            elif center[0] >= 780 and center[0] <= 980:
                pygame.mixer.Sound('drum sound/Hi-Hat-Open-Hit.mp3').play()  # playing the .wav file
                time.sleep(0.08)
                pygame.mixer.Sound('drum sound/Hi-Hat-Open-Hit.mp3').stop()

            elif center[0] >= 540 and center[0] <= 740:
                pygame.mixer.Sound('drum sound/Floor-Tom-Drum-Hit.mp3').play()  # playing the .wav file
                time.sleep(0.08)
                pygame.mixer.Sound('drum sound/Floor-Tom-Drum-Hit.mp3').stop()

            elif center[0] >= 1020 and center[0] <= 1220:
                pygame.mixer.Sound('drum sound/Snare-Drum-Hit.mp3').play()  # playing the .wav file
                time.sleep(0.08)
                pygame.mixer.Sound('drum sound/Snare-Drum-Hit.mp3').stop()



    frame = cv.flip(frame, 1)

    # outtput
    cv.imshow('Frame', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()