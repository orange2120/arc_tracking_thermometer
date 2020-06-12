'''
Haar Cascade Face detection with OpenCV  
    Based on tutorial by pythonprogramming.net
    Visit original post: https://pythonprogramming.net/haar-cascade-face-eye-detection-python-opencv-tutorial/  
Adapted by Marcelo Rovai - MJRoBot.org @ 7Feb2018 
'''

import numpy as np
import cv2
import serial

COM_PORT = '/dev/ttyS0'
BAUD_RATE = 115200
ser = serial.Serial(COM_PORT, BAUD_RATE)

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades
faceCascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height

while True:
    ret, img = cap.read()
    img = cv2.flip(img, -1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        
        scaleFactor=1.2,
        minNeighbors=5,     
        minSize=(10, 10)
    )

    for (x,y,w,h) in faces:
        point = f'{x},{y}\n'
        
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.putText(img, point, (x, y), cv2.FONT_HERSHEY_SIMPLEX,
  1, (255, 255, 255), 1, cv2.LINE_AA)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
        # fps = cap.get(cv2.CAP_PROP_FPS)
        # print(f'FPS: {fps}')
        print(point, end='')

        ser.write(point.encode())
        

    cv2.imshow('video',img)

    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break

ser.close()
cap.release()
cv2.destroyAllWindows()
