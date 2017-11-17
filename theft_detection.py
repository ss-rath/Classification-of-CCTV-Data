'''
Developed by Group-5
PD Lab
Autumn 2017-18
NIT,Rourkela
'''

def theft_detection():
	# import the necessary packages
	import datetime
	import imutils
	import time
	import cv2
	import serial
	import tkMessageBox

	try:
		ser=serial.Serial('/dev/ttyUSB0', 9600) #open the serial port in linux 
		#ser=serial.Serial('COM6', 9600) #open the serial portin windows
	except:
		tkMessageBox.showinfo("Error!", "Please connect the arduino and verify the device mount point")
		return 0
		
	cam = cv2.VideoCapture(0) #open the camera device
	time.sleep(0.25) #delay for 0.25s


	firstFrame = None


	while True:
		
		_, frame = cam.read() #get the frame
		frame=cv2.flip(frame,1) #flip the frame

		if not _:
			break


		frame = imutils.resize(frame, width=500) #resie the frame
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #change the colourspace to grayscale
		gray = cv2.GaussianBlur(gray, (21, 21), 0) #make gaussian blur


		if firstFrame is None: #in case the camera doesn't open
			firstFrame = gray
			continue

		frameDelta = cv2.absdiff(firstFrame, gray) #background subtraction
		thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1] #bit-wise thresholding of the image matrix
		thresh = cv2.dilate(thresh, None, iterations=2) #dilation of the image
		image, cnts, ssr = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE) #function to find the required contours
		
		count = 0 #for keeping count of objects

		for c in cnts:
			
			if cv2.contourArea(c) < 3:
				continue
			if cv2.contourArea(c) > 50:
				count+=1
		
			(x, y, w, h) = cv2.boundingRect(c)
			cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2) #draw rectangle over the motion

		
		if count==0:
			ser.write('a')
		if count!=0:
			ser.write('f')
			

		cv2.imshow("Theft detection PD Lab Group-5", frame)
		key = cv2.waitKey(1) & 0xFF

		# if the 'q' key is pressed, break from the loop
		if key == ord("q"):
			break

	cam.release()
	ser.close()
	cv2.destroyAllWindows()
