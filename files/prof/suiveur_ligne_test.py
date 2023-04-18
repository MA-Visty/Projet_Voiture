#!/usr/bin/env python
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering  
GPIO.setup(20, GPIO.IN)    # set GPIO16 as input (line follower)  
  
try:  
    while True:            # this will carry on until you hit CTRL+C  
        if GPIO.input(20): # if port 16 == 1  
            print ("Port 16 is 1/HIGH/True - LED ON" )   
        else:  
            print ("Port 16 is 0/LOW/False - LED OFF")  
        sleep(0.5)         # wait 0.5 seconds  
  
finally:                   # this block will run no matter how the try block exits  
    GPIO.cleanup()         # clean up after yourself

