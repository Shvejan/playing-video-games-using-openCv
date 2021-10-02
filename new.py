import cv2
import imutils
import numpy as np
blue=np.array([105,93,40,143,247,255])
pink=np.array([149,52,46,178,226,255])
yellow=np.array([20,101,98,30,255,255])
video=cv2.VideoCapture(0)

while True:
    _,frame=video.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    blue_mask=cv2.inRange(hsv,blue[:3],blue[3:])
    pink_mask=cv2.inRange(hsv,pink[:3],pink[3:])
    yellow_mask=cv2.inRange(hsv,yellow[:3],yellow[3:])


    blue_cont=cv2.findContours(blue_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    pink_cont=cv2.findContours(pink_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    yellow_cont=cv2.findContours(yellow_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    blue_points=imutils.grab_contours(blue_cont)
    pink_points=imutils.grab_contours(pink_cont)
    yellow_points=imutils.grab_contours(yellow_cont)


    lis=[blue_points,pink_points,yellow_points]

    count=[0,0,0]
    for i,color in enumerate(lis):
        for c in color:
            if cv2.contourArea(c)>150:
                cv2.drawContours(frame,[c],-1,(0,255,0),3)
                count[i]=count[i]+1
                if(i==0):
                    M=cv2.moments(c)
                    x=int(M['m10']/M['m00'])
                    y=int(M['m01']/M['m00'])
                    cv2.circle(frame,(x,y),5,(255,255,0),5)

    if( count[0]==1 and count[1]==1 and count[2]==1 and lis[0] and lis[1] and lis[2]):
        cv2.putText(frame,'stop',(50,350),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
    elif(count[0]==1 and count[1]==1 and lis[0] and lis[1]):
        cv2.putText(frame,'right',(50,200),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
    elif(count[1]==1 and count[2]==1 and lis[0] and lis[2]):
        cv2.putText(frame,'left',(50,250),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
    elif(count[1]==1 and count[2]==1 and lis[1] and lis[2]):
        cv2.putText(frame,'jump',(50,300),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
    elif(count[0]==1 and lis[0]):
        cv2.putText(frame,'aim',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
    elif(count[1]==1 and lis[1]):
        cv2.putText(frame,'shoot',(50,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
    elif(count[2]==1 and lis[2]):
        cv2.putText(frame,'forward',(50,150),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)



    cv2.imshow('frame',frame)

    if cv2.waitKey(1)&0xFF==ord('a'):
        break
video.release()
cv2.destroyAllWindows()
