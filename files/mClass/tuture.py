import RPi.GPIO as GPIO
import time
import os
from mClass.motorDC import DC
from mClass.servoMotor import PAPA
from mClass.sensorInfrared import Infrared
from mClass.sensorUltraSonic import UltraSonic

class Car:
	def __init__(self):
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
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
		self.sL = UltraSonic(11, 9)
		# Sensor "UltraSonic" Front
		self.sF = UltraSonic(6, 5)
		# Sensor "UltraSonic" Right
		self.sR = UltraSonic(26, 19)

		# Sensor "INfrared"
		self.sI = Infrared(20)
	
	def start(self):
		speed = 60
		mtime = 10
		try:
			"""
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

			self.sI.start()

			while not self.sI.getValue():
				print("Distance left:", self.sL.getDistance(), "cm")
				print("Distance front:", self.sF.getDistance(), "cm")
				print("Distance right:", self.sR.getDistance(), "cm")
				time.sleep(0.75)
				os.system("clear")

			self.sI.start()
		finally:
			self.direction.reset()

			self.mL.setSpeed(0)
			self.mR.setSpeed(0)

			self.sL.stop()
			self.sF.stop()
			self.sR.stop()

			self.sI.stop()