import RPi.GPIO as GPIO
from threading import Thread
import time

class Infrared(Thread):
	def __init__(self, _pin):
		super().__init__()
		self.pin = _pin
		self.value = 0
		self.isKilled = False

	def update(self):
		self.value = GPIO.input(self.pin)
	
	def run(self):
		# Set up the GPIO pins
		GPIO.setup(self.pin, GPIO.IN)

		while not self.isKilled:
			self.update()
			time.sleep(0.1)

		print(self, " is killed")

	def stop(self):
		self.isKilled = True

	def getValue(self):
		return self.value