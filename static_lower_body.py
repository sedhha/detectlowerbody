import numpy as np
import cv2
image_path="1.jpg"
image=cv2.imread(image_path)
scale=0.5
if(np.shape(image)[0]>=600 or np.shape(image)[1]>=600):
    image=cv2.resize(image,(int(np.shape(image)[1]*scale),int(np.shape(image)[0]*scale)))
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
roi_color=image.copy()
upper_body_cascade=cv2.CascadeClassifier('haarcascade_fullbody.xml')
lower_body_cascade = cv2.CascadeClassifier('haarcascade_lowerbody.xml')
body_full = lower_body_cascade.detectMultiScale(gray, 1.1, 3)
print(body_full)
for (ex,ey,ew,eh) in body_full:
    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
cv2.imshow("ROI",roi_color)
cv2.imwrite("Result1.png",roi_color)
