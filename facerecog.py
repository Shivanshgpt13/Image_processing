#!/usr/bin/python2
import cv2
import numpy as np
#loading face xml database
face_cascade=cv2.CascadeClassifier('face.xml')
# start web cam
cap=cv2.VideoCapture(0)


while(cap.isOpened()) :
	#reading camera frame
	status,img=cap.read()
	#converting color image to grayscale image
	grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	#trying multiangle in grayscaled image  #tunning parameter
	
	faces=face_cascade.detectMultiScale(grayimg,1.15,5)
	print(faces)
	for (x,y,w,h) in faces :
		if x >0 and y > 0 and w > 0 and h > 0 :
			print ("Face Detected !!!!!!!!!!!!!!!!!!!!!!!")
	# applying for iteration in multiscaled variable
	for(x,y,w,h) in faces :
	     cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
	     roi_gray=grayimg[y:y+h,x:x+w]
	     roi_color=img[y:y+h,x:x+w]
	
	cv2.imshow('Camera',img)
	if cv2.waitKey(30) & 0xFF == ord('q'):
	      break

cap.release()
cv2.destroyAllWindows()		

