import cv2
import datetime

cap=cv2.VideoCapture(0)

cap.set(3, 700)  #width
cap.set(4, 700)  #height

while(cap.isOpened()):
    ret,frame=cap.read()
    if(ret==True):

        font=cv2.FONT_HERSHEY_TRIPLEX
        text='Width : '+str(cap.get(3))+' Height : '+str(cap.get(4))
        date=str(datetime.datetime.now())
        frame=cv2.putText(frame,text,(10,50), font, 1, (0,100,255), 2)
        frame = cv2.putText(frame, date, (10, 90), font, 1, (0, 100, 255), 2)
        cv2.imshow('Frame_NAME', frame)
        if cv2.waitKey(1) & 0xFF== ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()