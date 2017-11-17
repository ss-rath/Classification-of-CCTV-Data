'''
Developed by Group-5
PD Lab
Autumn 2017-18
NIT,Rourkela
'''

def pedestrian_detection():
	#import the necessary packages
	from imutils.object_detection import non_max_suppression
	import cv2
	import imutils
	import numpy as np
	import tkMessageBox

	hog = cv2.HOGDescriptor() #create an instance of the HOGDescriptor class
	hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector()) #use the People Detector function of the class
	imagePath="img7.jpg" #path of the image. this may also be replaced with the numpy array that we get from a camera feed
	image = cv2.imread(imagePath)
	image = imutils.resize(image, width=min(400, image.shape[1]))#resizing the image
	orig = image.copy()

	# detect people in the image
	(rects, weights) = hog.detectMultiScale(image, winStride=(2,2), padding=(4,4), scale=1.05) #change this to calibrate
	rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects]) #this is a numpy array of the coordinates of the rectangles that are made to highlight the portions of the image
	pick = non_max_suppression(rects, probs=None, overlapThresh=0.50) #non-max supression algorithm is used to avoid detection of a subset contour inside a big contour twice

	# draw the final bounding boxes
	for (xA, yA, xB, yB) in pick:
		cv2.rectangle(image, (xA, yA), (xB, yB), (255, 0, 0), 2) #draw the rectangles

	font = cv2.FONT_HERSHEY_SIMPLEX
	positionofText = (orig.shape[1]-220,orig.shape[0]-12)
	fontScale              = 0.75
	fontColor              = (0,0,0)
	lineType               = 2
	
	#if there is some difference between the output after non max compression and without it
	if(len(pick) != len(rects)):
		cv2.putText(image,'Pedastrians: '+str(len(pick))+"-"+str(len(rects)), positionofText, font, fontScale,fontColor,lineType)
	
	else:
		cv2.putText(image,'Pedastrians: '+str(len(pick)), positionofText, font, fontScale,fontColor,lineType)
	cv2.imshow("Pedestrian Detection", image)

	cv2.waitKey(0)
