import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
pinList=[26,19,13,6,5,21,20,16]

for i in pinList:
    GPIO.setup(i,GPIO.OUT)



def oneByOne(rpt,delay):
      for j in range(0,rpt):
            for i in pinList:
                GPIO.output(i,GPIO.HIGH)
                print(" Led "+str(i)+" on \n")
                time.sleep(delay)
                GPIO.output(i,GPIO.LOW)
                print(" Led  "+str(i)+" off \n")
      print("Quit")

oneByOne(int(2),float(.5))
