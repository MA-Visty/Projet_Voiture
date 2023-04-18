import RPi.GPIO as GPIO
import time
import os
from mClass.motorDC import DC
from mClass.servoMotor import PAPA
from mClass.sensorInfrared import Infrared
from mClass.sensorUltraSonic import UltraSonic

class Car:
	def __init__(self):
		try:
			GPIO.setmode(GPIO.BCM) # Board->BCM

			# Motor Left
			self.mL = DC(10, 24, 4)  # 19->10 ; 18->24 ; 
			# Motor Right
			self.mR = DC(17, 23, 5)  # 17->17 ; 16->23 ;
			# Servo Motor
			#self.direction = PAPA()

			# Sensor "UltraSonic" Left
			self.sL = UltraSonic(11, 9) # 23->11 ; 21->9
			# Sensor "UltraSonic" Front
			self.sF = UltraSonic(6, 5) # 31->6 ; 29->5
			# Sensor "UltraSonic" Right
			self.sR = UltraSonic(26, 19) # 37->26 ; 35->19

			# Sensor "Infrared"
			self.sI = Infrared(20)

			# Sensor "RGB"  ===>  NOT TODAY
			#self.sC = Color()
		finally:
			GPIO.cleanup()
	
	def start(self):
		try:
			self.mL.forward()
			self.mR.forward()
			self.sL.start()
			self.sF.start()
			self.sR.start()

			self.sI.start()

			while not self.sI.getValue():
				print("Distance left:", self.sL.getDistance(), "cm")
				print("Distance front:", self.sF.getDistance(), "cm")
				print("Distance right:", self.sR.getDistance(), "cm")
				time.sleep(0.2)
				os.system("clear")
		finally:
			self.sL.stop()
			self.sF.stop()
			self.sR.stop()
			self.mL.stop()
			self.mR.stop()
			self.sI.stop()