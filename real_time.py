import numpy as np
import cv2
cam=cv2.VideoCapture(0)
upper_body_cascade=cv2.CascadeClassifier('haarcascade_fullbody.xml')
lower_body_cascade = cv2.CascadeClassifier('haarcascade_lowerbody.xml')
while True:
    _,image=cam.read()
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    roi_color=image.copy()
    body_full = lower_body_cascade.detectMultiScale(gray, 1.1, 3)
#print(body_full)
    for (ex,ey,ew,eh) in body_full:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    cv2.imshow("ROI",roi_color)
    k=cv2.waitKey(1)
    if k & 0xFF==ord('q'):
        break
