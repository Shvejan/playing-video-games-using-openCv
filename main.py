import cv2
import numpy as np
import imutils

vdo = cv2.VideoCapture(0)



green_range = np.array([73, 104, 77, 90, 200, 199])
blue_range =np.array( [102 ,111 ,120 ,117 ,156 ,195])
while True:
    _, frame = vdo.read()


    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    green_mask = cv2.inRange(hsv,green_range[:3],green_range[3:])
    blue_mask = cv2.inRange(hsv,blue_range[:3],blue_range[3:])

    green_cnt = cv2.findContours(green_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    blue_cnt = cv2.findContours(blue_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    green_points = imutils.grab_contours(green_cnt)
    blue_points = imutils.grab_contours(blue_cnt)
    
    list_of_all_points = [green_points,blue_points]
    
    detected_colors = [0,0]
    
    position_of_green = 0
    
    
    for i,color in enumerate(list_of_all_points):
        for c in color:
            if cv2.contourArea(c) >150:
                cv2.drawContours(frame,[c],-1,(0,255,0),3)
                detected_colors[i]=1
                
                if(i==0):
                    m=cv2.moments(c)
                    x = int(m['m10']/m['m00'])
                    y = int(m['m01']/m['m00'])
                    position_of_green= (x,y)
                    cv2.circle(frame, (x,y), 5, (255,0,255), 5)
                
    
    if(detected_colors[0]):
        cv2.putText(frame, 'aim', (50,50), cv2.FONT_HERSHEY_SIMPLEX, 
                   1, (0,0,0), 2)

    if(detected_colors[1]):
        cv2.putText(frame, 'shoot', (50,100), cv2.FONT_HERSHEY_SIMPLEX, 
                   1, (0,0,0), 2)

    
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) ==13:
        break
    
vdo.release()
cv2.destroyAllWindows()