'''
Developed by Group-5
PD Lab
Autumn 2017-18
NIT,Rourkela
'''


def vehicle_detector():
	import cv2
	import tkMessageBox

	try:
		cap = cv2.VideoCapture('video.avi') #get the frames from the video/camera
	except:
		tkMessageBox.showinfo("Error!", "Video feed not available")
	try:
		car_cascade = cv2.CascadeClassifier('cars.xml') #use the cascade classifier function for the haar algorithm
	except:
		tkMessageBox.showinfo("Error!", "Cascade classifier file not available")
	while True:
		ret, frames = cap.read()
		if ret:
			gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
			cars = car_cascade.detectMultiScale(gray, 1.1, 1)
		else:
			cv2.destroyAllWindows()
			break
		for (x,y,w,h) in cars:
			cv2.rectangle(frames,(x,y),(x+w,y+h),(255,0,0),2)

		cv2.imshow('Vehicle Detection', frames) 
		# Wait for Esc key to stop
		if cv2.waitKey(33) == 27:
			break
	
	cv2.destroyAllWindows()
	return 0
