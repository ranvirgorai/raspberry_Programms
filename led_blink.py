import RPi.GPIO as GPIO
import time
# blinking function
def blink(pin):
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin,GPIO.LOW)
    time.setup(1)
    return
# to use raspberry pi board pin numbers
GPIO.setmode(GPIO.BOARD)
#setup GPIO output channel
GPIO.setup(11,GPIO.OUT)
# BLINK gpio 11 50 times
i=0
for i in range (5):
    blink(11)
    GPIO.cleanup()
GPIO.setwarnings(False)
