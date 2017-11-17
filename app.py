'''
Developed by Group-5
PD Lab
Autumn 2017-18
NIT,Rourkela
'''

#importing the local and the installed packages
from motion_detector import *
from theft_detection import *
from pedestrian_detection import *
from vehicle_detection import *
from centroid_detection import *
from tailgating_detection import *
import thread
import tkMessageBox
from Tkinter import *

#functions which are called when buttons are clicked
def func1():
	try:
		thread.start_new_thread(motion_detector,()) #fill the empty tuple with arguments if needed in future
	except:
		tkMessageBox.showinfo("Error!", "Some error in the code")
	
def func2():
	try:
		thread.start_new_thread(theft_detection,())
	except:
		tkMessageBox.showinfo("Error!", "Some error in the code")
	
def func3():
	try:
		thread.start_new_thread(pedestrian_detection,())
	except:
		tkMessageBox.showinfo("Error!", "Some error in the code")
		
	
def func4():
	try:
		thread.start_new_thread(vehicle_detector,())
	except:
		tkMessageBox.showinfo("Error!", "Some error in the code")
			
def func5():
	try:
		thread.start_new_thread(centroid_detector,())
	except:
		tkMessageBox.showinfo("Error!", "Some error in the code")

def func6():
	try:
		thread.start_new_thread(tailgating_detector,())
	except:
		tkMessageBox.showinfo("Error!", "Some error in the code")
		

def main(): #main loop
	

	root=Tk() #instance of Tk class
	root.geometry("580x400") #setting the geometry of the window
	root.title("Deploy Algorithm") #title of the window

#creating the buttons in the window
	button1 = Button(root, height=5, width=20, text="Motion Detection", command= func1)
	button1.place(x=100, y=50)

	button2 = Button(root, height=5, width=20, text="Theft Detection", command= func2)
	button2.place(x=100, y=150)

	button3 = Button(root, height=5, width=20, text="Pedestrian Detection", command=func3)
	button3.place(x=100, y=250)
	
	button4 = Button(root, height=5, width=20, text="Vehicle Detection", command=func4)
	button4.place(x=320, y=50)
	
	button5 = Button(root, height=5, width=20, text="Centroid Detection", command=func5)
	button5.place(x=320, y=150)
	
	button5 = Button(root, height=5, width=20, text="Tailgating Detection", command=func6)
	button5.place(x=320, y=250)
	root.mainloop() #start the mainloop

main()
