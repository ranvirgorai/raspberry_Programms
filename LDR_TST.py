#Created By Ranvir 05/06/2016
#Cpmponent Required LDR, CAPACITOR 1uF, LED

import RPi.GPIO as GPIO, time, os
DEBUG=1
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)		#SETUP LED PIN
GPIO.output(4,GPIO.LOW)

def LDRreading(RCpin):			#FUNCTION TO READ LDR READING
    reading=0					#LDR READING VARIABLE	
    GPIO.setup(RCpin,GPIO.OUT)	
    GPIO.output(RCpin,GPIO.LOW)
    time.sleep(.1)

    GPIO.setup(RCpin,GPIO.IN)				#ENABLED LDR PIN AS INPUT
    while (GPIO.input(RCpin)==GPIO.LOW):	#READING LDR PIN WHILE IT IS LOW
        reading+=2							#INCRASING LDR VLAUE
    return reading

while True:									#LOOPING LDR READING FUNCTION
    light=LDRreading(3)
    print(light)
    if(light<2500):							#SETTING MAXIMUM VALUE TURN OFF LED
        GPIO.output(4,GPIO.LOW)
    if(light>3500):							#SETTING MINIMAL VALUE TURN ON LED
        GPIO.output(4,GPIO.HIGH)
    
