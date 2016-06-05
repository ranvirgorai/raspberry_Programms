#Created By Ranvir 05/06/2016

#In this porgramm we going to control a RGB LED
#Connect LED -ve terminal as comman 
#RED -  2
#GREEN -3
#BLUE - 4

import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)
gpio.setup(2,gpio.OUT)
gpio.setup(3,gpio.OUT)
gpio.setup(4,gpio.OUT)
p1=gpio.PWM(2,50)      #p1 is associated with the GPIO pin with frequency as 50Hz
p2=gpio.PWM(3,50)
p3=gpio.PWM(4,50)
p1.start(0)				#p1 is Enabled for output
p2.start(0)
p3.start(0)
delay=.01
while True:
    for i in range (100):
        p1.ChangeDutyCycle(i)		#Changing Dutycycle value to control intensity or Red Led
        time.sleep(delay)
    print("RED")
    for i in range (100):
        p1.ChangeDutyCycle(100-i)
        time.sleep(delay)

    for i in range (100):
        p2.ChangeDutyCycle(i)
        time.sleep(delay)
    print("GREEN")
    for i in range (100):
        p2.ChangeDutyCycle(100-i)
        time.sleep(delay)
    for i in range (100):
        p3.ChangeDutyCycle(i)
        time.sleep(delay)
    print("BLUE")
    for i in range (100):
        p3.ChangeDutyCycle(100-i)
        time.sleep(delay)

    for i in range (100):
        p1.ChangeDutyCycle(i)
        p2.ChangeDutyCycle(i)
        time.sleep(delay)
    print("YELLOW")
    for i in range (100):
        p1.ChangeDutyCycle(100-i)
        p2.ChangeDutyCycle(100-i)
        time.sleep(delay)

    for i in range (100):
        p2.ChangeDutyCycle(i)
        p3.ChangeDutyCycle(i)
        time.sleep(delay)
    print("CYEN")
    for i in range (100):
        p2.ChangeDutyCycle(100-i)
        p3.ChangeDutyCycle(100-i)
        time.sleep(delay)

    for i in range (100):
        p1.ChangeDutyCycle(i)
        p3.ChangeDutyCycle(i)
        time.sleep(delay)
    print("PURPLE")
    for i in range (100):
        p1.ChangeDutyCycle(100-i)
        p3.ChangeDutyCycle(100-i)
        time.sleep(delay)

    for i in range (100):
        p1.ChangeDutyCycle(i)
        p2.ChangeDutyCycle(i)
        p3.ChangeDutyCycle(i)
        time.sleep(delay)
    print("WHITE")
    for i in range (100):
        p1.ChangeDutyCycle(100-i)
        p2.ChangeDutyCycle(100-i)
        p3.ChangeDutyCycle(100-i)
        time.sleep(delay)
							
gpio.cleanup()						#At End all pin are flushed
    


