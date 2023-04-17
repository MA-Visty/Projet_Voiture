import RPi.GPIO as GPIO
from Motors import *
from Sensors import *

class Car:
	def __init__(self):
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

		# Sensor "RGB"
		self.sC = Color()
		# Sensor "Infrared"
		self.sI = Infrared(20)

if __name__ == "__main__":
	try:
		GPIO.setmode(GPIO.BCM)

		tuture = Car()

		while True:
			tuture.sL.getDistance()
			tuture.sF.getDistance()
			tuture.sR.getDistance()

			tuture.sI.getInfo()

			#12 14
			#11 13 15
	finally:
		GPIO.cleanup()