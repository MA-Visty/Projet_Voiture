import RPi.GPIO as GPIO
import time
import os
from mClass.motorDC import DC
from mClass.servoMotor import PAPA
from mClass.sensorInfrared import Infrared
from mClass.sensorUltraSonic import UltraSonic

class Car:
	def __init__(self):
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
		# Motor Left
		self.mL = DC(24, 23, 5)
		# Motor Right
		self.mR = DC(27, 22, 4)
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
	
	def start(self):
		try:
			self.direction.position = self.direction.maxPulse
			self.direction.update()
			
			time.sleep(0.5)

			self.mL.forward()
			self.mL.setSpeed(100)
			self.mR.forward()
			self.mR.setSpeed(100)
			
			time.sleep(5)

			self.mL.setSpeed(0)
			self.mR.setSpeed(0)

			time.sleep(0.5)

			self.direction.position = self.direction.midPulse
			self.direction.update()

			time.sleep(0.5)

			self.mL.forward()
			self.mL.setSpeed(100)
			self.mR.forward()
			self.mR.setSpeed(100)

			time.sleep(5)

			self.mL.setSpeed(0)
			self.mR.setSpeed(0)

			time.sleep(0.5)
		finally:
			self.direction.reset()

			self.mL.setSpeed(0)
			self.mR.setSpeed(0)