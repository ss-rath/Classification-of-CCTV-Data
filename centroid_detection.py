'''
Developed by Group-5
PD Lab
Autumn 2017-18
NIT,Rourkela
'''

# defining the function
def centroid_detector():
	#import the necessary modules
	import cv2
	import tkMessageBox

	try:
		cap = cv2.VideoCapture('video.avi')
	except:
		tkMessageBox.showinfo("Error!", "Video feed not available")
	try:
		car_cascade = cv2.CascadeClassifier('cars.xml')
	except:
		tkMessageBox.showinfo("Error!", "Cascade classifier file not available")
	while True:
		ret, frames = cap.read() #this function returns the frames from either the video file or the video device
		if ret:
			gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY) #frames converted to grayscale for faster execution of haar algorithm
			cars = car_cascade.detectMultiScale(gray, 1.1, 1)
			# the arguments of the above function are very important. The first argument is the grayscale frame.
			# the second argument of the function is the scaling factor of the frame. This should be changed based on the size of the frame.
			# the third argument of the function is the minimum distance from the neighbour object.
			# both these values must be chosen by trial and error to get the best results.
		else:
			cv2.destroyAllWindows()
			break
			return 0
		for (x,y,w,h) in cars:
			cv2.circle(frames,(x+(w/2),y+(h/2)), 4, (0,0,255), -1)

		cv2.imshow('Centroid Detection', frames) 
		# Wait for Esc key to stop
		if cv2.waitKey(33) == 27:
			break
			return 0
	
	cv2.destroyAllWindows() #destroy all the windows
	return 0
