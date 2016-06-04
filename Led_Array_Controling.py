# Created by RANVIR 04/06/16
#While confi Hardware keep -ve Terminal of Led pin is comman
#And connect +ve termina to each pin Of GPIO
#As arrange your led accoroding to that place gpio pin list in Pinlist variable
 

import RPi.GPIO as GPIO					# Importing RPi as Gpio
import time								#importing time for dealy control
GPIO.setmode(GPIO.BCM)					#setting board mode as Board/BCM
pinList=[26,19,13,6,5,21,20,16]			#Output Pin Decleration

for i in pinList:						# setting pin out put
    GPIO.setup(i,GPIO.OUT)



def oneByOne(rpt,delay):								#Function to glow led on by one
      for j in range(0,rpt):							#Outer loop to controle no of itiration
            for i in pinList:							#Inner loop to controle Led Output
                GPIO.output(i,GPIO.HIGH)
                print(" Led "+str(i)+" on")
                time.sleep(delay)
                GPIO.output(i,GPIO.LOW)
                print(" Led  "+str(i)+" off")
      print("Quit")

#oneByOne(int(rep),float(delay))

def allOnOneByOne(rpt,delay):							#Function to glow led on onc all on then off
      for j in range(0,rpt):							#Outer loop to controle no of itiration
            for i in pinList:							#Inner loop to turn On Led
                GPIO.output(i,GPIO.HIGH)
                print(" Led  "+str(i)+" on")
                time.sleep(delay)
            for i in pinList:							#Inner loop to turn Off Led
                GPIO.output(i,GPIO.LOW)
                print(" Led  "+str(i)+" off")
                time.sleep(delay)
      print("Quit")

#allOnOneByOne(int(rep),float(delay))

def mainfun():											#Main Function to control user choice
    men=raw_input("Menu: Please Enter Your Choice \n 1. for One By One Scan \n 2. For On All Onec Then Off \n ")
    if(int(men)==1):									#if User Gives Input 1 then Calling first function
        rep=raw_input("Enter No Of Repetation= ")
        delay=raw_input("Enter delay In Sec= ")
        oneByOne(int(rep),float(delay))
    else:												#if User Gives Input 2 then Calling Second function
        rep=raw_input("Enter No Of Repetation= ")
        delay=raw_input("Enter delay In Sec= ")
        allOnOneByOne(int(rep),float(delay))
    GPIO.cleanup()

mainfun()												#calling Main function							
