'''
Project: Earthrover Robot
Author: Jitesh Saini
Github: https://github.com/jiteshsaini
website: https://helloworld.co.in

'''



import os, time

edgetpu=0 # If Coral USB Accelerator connected, then make it '1' otherwise '0'

m1_1 = 8
m1_2 = 11
m2_1 = 14 
m2_2 = 15 
cam_light = 17
headlight_right = 18
headlight_left = 27 
sp_light=9 


def init_gpio():
	print("finish setup")
	

def back():
    print("moving back!!!!!!")
    
    
def right():
	print("Moving right")
	

def left():
	print("Moving left")
	
def forward():
	print("Moving forward")
	# Here is where all of the robot interfacing occurs
	
def stop():
	print("Stopping")

def speak_tts(text,gender):
	cmd="python /var/www/html/earthrover/speaker/speaker_tts.py '" + text + "' " + gender + " &"
	os.system(cmd)
	
def camera_light(state):
	if(state=="ON"):
		print("light on")
	else:
		print("light off")
		
def head_lights(state):
	if(state=="ON"):
		print("light on")
	else:
		print("light off")
		
def red_light(state):
	if(state=="ON"):
		print("light on")
	else:
		print("light off")
	
