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

		# Sensor "UltraSonic" Left
		self.sL = UltraSonic(23, 21)
		# Sensor "UltraSonic" Front
		self.sF = UltraSonic(31, 29)
		# Sensor "UltraSonic" Right
		self.sR = UltraSonic(37, 35)

		# Sensor "INfrared"
		self.sI = Infrared(20)
	
	def start(self):
		speed = 60
		mtime = 10
		try:
			self.direction.position = self.direction.maxPulse
			self.direction.update()
			
			time.sleep(0.5)

			self.mL.forward()
			self.mL.setSpeed(speed)
			self.mR.forward()
			self.mR.setSpeed(speed)
			
			time.sleep(mtime)

			self.mL.setSpeed(0)
			self.mR.setSpeed(0)

			time.sleep(0.5)

			self.direction.position = self.direction.midPulse
			self.direction.update()

			time.sleep(0.5)

			self.direction.position = self.direction.minPulse
			self.direction.update()

			time.sleep(0.5)

			self.mL.forward()
			self.mL.setSpeed(speed)
			self.mR.forward()
			self.mR.setSpeed(speed)

			time.sleep(mtime)

			self.mL.setSpeed(0)
			self.mR.setSpeed(0)

			time.sleep(0.5)

			"""
			self.sL.start()
			self.sF.start()
			self.sR.start()

			while not self.sI.getValue():
				print("Distance Left:", self.sL.getDistance(), " cm")
				print("Distance Left:", self.sF.getDistance(), " cm")
				print("Distance Left:", self.sR.getDistance(), " cm")
				
				time.sleep(0.75)

			self.sI.start()
			"""
		finally:
			self.direction.reset()

			self.mL.setSpeed(0)
			self.mR.setSpeed(0)

			self.sL.stop()
			self.sF.stop()
			self.sR.stop()

			self.sI.stop()