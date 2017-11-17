'''
Developed by Group-5
PD Lab
Autumn 2017-18
NIT,Rourkela
'''
#this is similar to finding the centroid. the extra thing implented in this code is to find the distance between any two centroids and detect a tailgating

def tailgating_detector():
	#importing the necessary packages
	import cv2
	import tkMessageBox
	import math

	try:
		cap = cv2.VideoCapture('video.avi') 
	except:
		tkMessageBox.showinfo("Error!", "Video feed not available")
	try:
		car_cascade = cv2.CascadeClassifier('cars.xml')
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
			return 0
		distances=[]
		#the next steps are the distances between the centroids
		for i in range(len(cars)):
			for j in range(len(cars)):
				x1,y1=cars[i][0], cars[i][1]
				x2,y2=cars[j][0], cars[j][1]
				distance= math.sqrt(abs(x2*x2-x1*x1))
				distances.append([i,j,distance])
		#checking if the distances are less than a certain threshold
		for i in distances:
			if i[2]<15 and i[2]>10:
				centre_x=(cars[i[0]][0]+cars[i[1]][0])/2
				centre_y=(cars[i[0]][1]+cars[i[1]][1])/2
				cv2.circle(frames,(centre_x,centre_y), 30, (0,0,255), 3)
		
		cv2.imshow('Tailgating Detection', frames) 
		# Wait for Esc key to stop
		if cv2.waitKey(33) == 27:
			break
			return 0
	
	cv2.destroyAllWindows()
	return 0


