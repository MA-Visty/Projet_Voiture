import RPi.GPIO as GPIO
import time
from motorDC import DC
from servoMotor import PAPA
from sensorInfrared import Infrared
from sensorUltraSonic import UltraSonic

class Car:
	def __init__(self):
		try:
			GPIO.setmode(GPIO.BCM)

			# Motor Left
			self.mL = DC(19, 18)  # 19-> ; 18-> ; 
			# Motor Right
			self.mR = DC(17, 16)  # 17-> ; 16-> ;
			# Servo Motor
			self.direction = PAPA()

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
			self.sL.start()
			self.sF.start()
			self.sR.start()

			while True:
				print("Distance:", self.sL.getDistance(), "cm")
				print("Distance:", self.sF.getDistance(), "cm")
				print("Distance:", self.sR.getDistance(), "cm")
				time.sleep(0.2)
		finally:
			self.sL.stop()
			self.sF.stop()
			self.sR.stop()