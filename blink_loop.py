# Created by RANVIR 29/05/16

import RPi.GPIO as gpio 		# Importing RPi as Gpio
import time						#importing time for dealy control
gpio.setmode(gpio.BOARD)		#setting board mode as Board/BCM
gpio.setup(7,gpio.OUT)			# setting pin out put

def blink(times,speed):			#definging function as blink
	for i in range (0,times):	#Loop of blink
		print("Loop "+str(i+1))
		gpio.output(7,True)
		time.sleep(speed)
		gpio.output(7,False)
		time.sleep(speed)
	print("Quit")								
gpio.cleanup()						#cleaning Gpio input (not menetry)

inp=raw_input("Enter no of times ")	#Taking input from user
speed=raw_input("Enter speed ")	

blink(int(inp),float(speed))		#calling blink function argument are passes

