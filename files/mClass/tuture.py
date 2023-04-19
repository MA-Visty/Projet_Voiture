import RPi.GPIO as GPIO
import time
from mClass.motorDC import DC
from mClass.servoMotor import PAPA
from mClass.sensorInfrared import Infrared
from mClass.sensorUltraSonic import UltraSonic

class Car:
	def __init__(self):
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)

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
	
	def move(self, speed):
		if(100 >= speed >= 10):
			self.mL.forward()
			self.mL.setSpeed(speed)
			self.mR.forward()
			self.mR.setSpeed(speed)
		elif(-100 <= speed <= -10):
			self.mL.backward()
			self.mL.setSpeed(abs(speed))
			self.mR.backward()
			self.mR.setSpeed(abs(speed))
		else:
			self.mL.setSpeed(0)
			self.mR.setSpeed(0)

	def turn(self, deg):
		if(150 <= deg <= 450):
			self.direction.setPosition(deg)
	
	def start(self):
		self.sL.start()
		self.sF.start()
		self.sR.start()
		self.sI.start()
	
	def stop(self):
		self.move(0)
		self.direction.position = self.direction.midPulse
		self.direction.update()

		self.sL.stop()
		self.sF.stop()
		self.sR.stop()
		self.sI.stop()

		GPIO.cleanup()