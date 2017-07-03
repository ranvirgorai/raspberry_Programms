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
                print(" Led "+str(i)+" on")
                time.sleep(delay)
                GPIO.output(i,GPIO.LOW)
                print(" Led  "+str(i)+" off")
      print("Quit")

#oneByOne(int(rep),float(delay))

def allOnOneByOne(rpt,delay):
      for j in range(0,rpt):
            for i in pinList:
                GPIO.output(i,GPIO.HIGH)
                print(" Led  "+str(i)+" on")
                time.sleep(delay)
            for i in pinList:
                GPIO.output(i,GPIO.LOW)
                print(" Led  "+str(i)+" off")
                time.sleep(delay)
      print("Quit")

#allOnOneByOne(int(rep),float(delay))

def mainfun():
    men=raw_input("Menu: Please Enter Your Choice \n 1. for One By One Scan \n 2. For On All Onec Then Off \n ")
    if(int(men)==1):
        rep=raw_input("Enter No Of Repetation= ")
        delay=raw_input("Enter delay In Sec= ")
        oneByOne(int(rep),float(delay))
    else:
        rep=raw_input("Enter No Of Repetation= ")
        delay=raw_input("Enter delay In Sec= ")
        allOnOneByOne(int(rep),float(delay))
    GPIO.cleanup()

mainfun()
