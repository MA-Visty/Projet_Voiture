import RPi.GPIO as GPIO
import time
import os
from mClass.servoMotor import PAPA
from mClass.sensorInfrared import Infrared
from mClass.sensorUltraSonic import UltraSonic

class Car:
	def __init__(self):
		try:
			GPIO.setwarnings(False)
			GPIO.setmode(GPIO.BCM)
			"""
				PIN motor 1 :
				17
				18
				4
				PIN motor 2 :
				27
				15
				5
				Ultrasonic Left :
				23
				21
				Ultrasonic Front :
				31
				29
				Ultrasonic Right :
				37
				35
				Infrared :
				20
			"""
			# Servomotor
			self.direction = PAPA()

			"""
			# Sensor "UltraSonic" Left
			self.sL = UltraSonic(23, 21)
			# Motor Left
			self.mL = DC(24,23,4)  # 19->10 ; 18->24 ; 
			# Motor Right
			self.mR = DC(27,22,5)  # 17->17 ; 16->23 ;
			# Servo Motor
			#self.direction = PAPA()
			"""
		finally:
			GPIO.cleanup()
	
	def start(self):
		try:
			mbool = False
			while True:
				if(mbool):
					self.direction.turn(right=True)
				else:
					self.direction.turn(left=True)

				if(self.direction.position == self.direction.maxPulse):
					mbool = True
				if(self.direction.position == self.direction.minPulse):
					mbool = False
		finally:
			self.direction.reset()