import cv2

video = cv2.VideoCapture(0)
colors = [[76, 89, 95, 147, 105, 191], [
   102 ,117 ,111 ,156 ,120 ,195], [119, 178, 59, 229, 255, 255]]


color_range = [76 ,89, 45, 118, 81, 148]


while True:
    _,frame =video.read()

    hue_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    mask = cv2.inRange(hue_image, (color_range[0],color_range[2],color_range[4]),
                       (color_range[1],color_range[3],color_range[5]))

    final = cv2.bitwise_and(frame,frame,mask=mask)
    
    cv2.imshow('original', frame)
    cv2.imshow('mask',final)

    if cv2.waitKey(1) ==13:
        break

video.release()
cv2.destroyAllWindows()
