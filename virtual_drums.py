import numpy as np
import cv2 as cv
import pygame
import time


def play_sound(x,y):
    if 300 <= y <= 500:
        if x >= 60 and x <= 260:
            pygame.mixer.Sound('drum sound/Floor-Tom-Drum-Hit.mp3').play()  # playing the .wav file
            time.sleep(0.08)
            pygame.mixer.Sound('drum sound/Floor-Tom-Drum-Hit.mp3').stop()

            # playsound('drum sound/Bass-Drum-Hit.mp3')

        elif x >= 300 and x <= 500:
            pygame.mixer.Sound('drum sound/Bass-Drum-Hit.mp3').play()  # playing the .wav file
            time.sleep(0.08)
            pygame.mixer.Sound('drum sound/Bass-Drum-Hit.mp3').stop()

        elif x >= 780 and x <= 980:
            pygame.mixer.Sound('drum sound/Hi-Hat-Closed-2.mp3').play()  # playing the .wav file
            time.sleep(0.08)
            pygame.mixer.Sound('drum sound/Hi-Hat-Closed-2.mp3').stop()

        elif x >= 540 and x <= 740:
            pygame.mixer.Sound('drum sound/Snare-Drum-Hit.mp3').play()  # playing the .wav file
            time.sleep(0.08)
            pygame.mixer.Sound('drum sound/Snare-Drum-Hit.mp3').stop()

        elif x >= 1020 and x <= 1220:
            pygame.mixer.Sound('drum sound/Hi-Hat-Open-Hit.mp3').play()  # playing the .wav file
            time.sleep(0.08)
            pygame.mixer.Sound('drum sound/Hi-Hat-Open-Hit.mp3').stop()

            """
    if 50 <= y <= 100  and 400<= x <= 800:
        sound = pygame.mixer.Sound('drum sound/Chinese_New_Year.mp3').play()  # playing the .wav file
        sound.set_volume(0.1)
        time.sleep(0.08)
        pygame.mixer.Sound('drum sound/Chinese_New_Year.mp3').stop()
    """

cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 2200)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 2000)

print(cap.get(cv.CAP_PROP_FRAME_WIDTH),cap.get(cv.CAP_PROP_FRAME_HEIGHT))

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

    #cv.rectangle(frame, (400,50), (800,100), blue, 3)

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lower_blue = np.array([88, 109, 121])        # [107, 151, 139]
    upper_blue = np.array([120, 250, 255])       # [127,120,255]

    mask1 = cv.inRange(hsv, lower_blue, upper_blue)
    mask = cv.erode(mask1, kernal, iterations=1)
    mask = cv.morphologyEx(mask, cv.MORPH_OPEN, kernal)
    mask = cv.dilate(mask, kernal, iterations=1)
    cv.imshow('BLUE', mask)

    bx, by = 0, 0
    b_center, b_radius = 0, 0

    contours_b, hirarchy = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    try:
        for i in range(10):
            b_center, b_radius = cv.minEnclosingCircle(contours_b[i])
            bx, by = int(b_center[0]), int(b_center[1])
            if cv.contourArea(contours_b[i]) > 2000:
                cv.circle(frame, (int(b_center[0]), int(b_center[1])), 10, (0, 255, 255), 3)
                break

    except:
        pass

    lower_green = np.array([60, 98, 30])   #[39,102,84]
    upper_green = np.array([93, 255, 255])  #[84,255,255]

    mask_g = cv.inRange(hsv, lower_green, upper_green)
    mask_g = cv.erode(mask_g, kernal, iterations=1)
    mask_g = cv.morphologyEx(mask_g, cv.MORPH_OPEN, kernal)
    mask_g = cv.dilate(mask_g, kernal, iterations=1)
    cv.imshow('GREEN', mask_g)

    gx, gy = 0, 0
    g_center, g_radius = 0, 0

    contours_g, hirarchy = cv.findContours(mask_g, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    try:
        for i in range(10):
            g_center, g_radius = cv.minEnclosingCircle(contours_g[i])
            gx, gy = int(g_center[0]), int(g_center[1])
            if cv.contourArea(contours_g[i]) > 2000:
                cv.circle(frame, (int(g_center[0]), int(g_center[1])), 10, (0, 255, 255), 3)
                break

    except:
        pass

    play_sound(gx, gy)
    play_sound(bx, by)


    frame = cv.flip(frame, 1)

    # outtput
    cv.imshow('Frame', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()