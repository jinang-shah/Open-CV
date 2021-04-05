import numpy as np
import cv2

def click_event(event,x,y,flags,param):
    if event==cv2.EVENT_MOUSEMOVE:
        text='x : '+ str(x)+', Y : ' +str(y)
        font=cv2.FONT_HERSHEY_TRIPLEX
        #cv2.putText(img,text,(x,y),font,1,(0,255,255),1)
        cv2.circle(img,(x,y),3,(0,255,200),3)
        cv2.imshow('Frame',img)

def draw_line(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),3,(0,200,255),-1)
        points.append((x,y))
        if len(points)>=2:
            cv2.line(img,points[-1],points[-2],(0,200,255), 1)
            cv2.imshow('Frame',img)



points=[]
img=np.zeros((512,512,3),np.uint8)
cv2.imshow('Frame', img)

#cv2.setMouseCallback('Frame',click_event)
cv2.setMouseCallback('Frame',draw_line)
cv2.waitKey(0)
cv2.destroyAllWindows()