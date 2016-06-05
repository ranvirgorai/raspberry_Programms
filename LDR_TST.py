# LDR, CAPACITOR 1uF, LED

import RPi.GPIO as GPIO, time, os
DEBUG=1
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
GPIO.output(4,GPIO.LOW)

def LDRreading(RCpin):
    reading=0
    GPIO.setup(RCpin,GPIO.OUT)
    GPIO.output(RCpin,GPIO.LOW)
    time.sleep(.1)

    GPIO.setup(RCpin,GPIO.IN)
    while (GPIO.input(RCpin)==GPIO.LOW):
        reading+=2
    return reading

while True:
    light=LDRreading(3)
    light/=100
    print(light)
    if(light<25):
        GPIO.output(4,GPIO.LOW)
    if(light>30):
        GPIO.output(4,GPIO.HIGH)
    
