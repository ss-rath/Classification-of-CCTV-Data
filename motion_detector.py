'''
Developed by Group-5
PD Lab
Autumn 2017-18
NIT,Rourkela
'''

def motion_detector():
	# import the necessary packages
	import datetime
	import imutils
	import time
	import cv2
	import serial
	import tkMessageBox
	
	try:
		ser=serial.Serial('/dev/ttyUSB0', 9600) #open the serial port in linux 
		#ser=serial.Serial('COM6', 9600) #open the serial port in windows
	except:
		tkMessageBox.showinfo("Error!", "Please connect the arduino and verify the device mount point")
		return 0
		
	cam = cv2.VideoCapture(0) # open the video device. the argument is the video device number.
	# 0 for integrated webcam, 1 for external webcam
	time.sleep(0.25) # pause for 0.25s


	firstFrame = None #initialise an empty variable where the first frame would be saved


	while True:
		
		_, frame = cam.read() # get the frames
		frame=cv2.flip(frame,1);

		if not _:
			break


		frame = imutils.resize(frame, width=500) # for resizing the frame
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # colourspace is converted to grayscale
		gray = cv2.GaussianBlur(gray, (21, 21), 0) #Gaussian blur is applied. It is a technique of blurring the frame.


		if firstFrame is None: #in case the camera doesn't open
			firstFrame = gray #initialise as a blank frame
			continue

		frameDelta = cv2.absdiff(firstFrame, gray) # find out the difference between the current frame and blank frame
		thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1] #does the thresholding bit wise to the numpy array
		thresh = cv2.dilate(thresh, None, iterations=2) #dilate the image
		image, cnts, ssr = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)#find the required contours in the image
		
		count = 0 #for keeping count of objects

		for c in cnts:
			
			if cv2.contourArea(c) < 3: 
				continue
			if cv2.contourArea(c) > 50:
				count+=1
		
			(x, y, w, h) = cv2.boundingRect(c)
			cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2) #draw rectangle over the motion
			
		#print count
		#print the required data through serial
		if count==0:
			ser.write('a')
		if count==1:
			ser.write('b')
		if count==2:
			ser.write('c')
		if count==3:
			ser.write('d')
		if count==4:
			ser.write('e')
		if count>=5:
			ser.write('f')	

		cv2.imshow("Motion Detector PD Lab Group-5", frame)
		firstFrame = gray
		key = cv2.waitKey(1) & 0xFF

		# if the 'q' key is pressed, break from the loop
		if key == ord("q"):
			break

	cam.release()
	ser.close()
	cv2.destroyAllWindows()
