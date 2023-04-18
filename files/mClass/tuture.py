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
			# Sensor "UltraSonic" Front
			self.sF = UltraSonic(31, 29)
			# Sensor "UltraSonic" Right
			self.sR = UltraSonic(37, 35)

			# Sensor "Infrared"
			self.sI = Infrared(20)
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

		"""
		try:
			self.sL.start()
			self.sF.start()
			self.sR.start()
			
			self.sI.start()

			while not self.sI.getValue():
				print("Distance left:", self.sL.getDistance(), "cm")
				print("Distance front:", self.sF.getDistance(), "cm")
				print("Distance right:", self.sR.getDistance(), "cm")
				time.sleep(0.2)
				#os.system("clear")
		except Exception as e:
			print(e)
		finally:
			self.sL.stop()
			self.sF.stop()
			self.sR.stop()

			self.sI.stop()
		"""