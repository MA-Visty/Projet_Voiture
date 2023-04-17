import RPi.GPIO as GPIO
import time

class Infrared:
	def __init__(self, _pin):
		self.pin = _pin

	def getInfo(self):
		# Set up the GPIO pins
		GPIO.setup(self.pin, GPIO.IN)

		time.sleep(0.1)
		print(GPIO.input(self.pin))