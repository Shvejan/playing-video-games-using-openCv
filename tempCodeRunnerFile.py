
                cv2.drawContours(frame,[c],-1,(0,255,0),3)
                count[i]=count[i]+1
                if(i==0):
                    M=cv2.moments(c)
                    x=int(M['m10']/M['m00'])
                    y=int(M['m01']/M['m00'])
                    cv2.circle(frame,(x,y),5,(255,255,0),5)

    if( count[0]==1 and count[1]==1 and count[2]==1 and lis[0] and lis[1] and lis[2]):
        cv2.putText(frame,'stop',(50,350),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)