import RPi.GPIO as GPIO
from threading import Thread
import time

class UltraSonic(Thread):
	def __init__(self, _pinTrig, _pinEcho, _intervalTime=1):
		super().__init__(target=self.run)
		self.pinTrig = _pinTrig
		self.pinEcho = _pinEcho
		self.intervalTime = _intervalTime
		self.isKilled = False
		self.distance = 0

	def update(self):
		# Send signal
		GPIO.output(self.pinTrig, GPIO.HIGH)
		time.sleep(0.00001)
		GPIO.output(self.pinTrig, GPIO.LOW)

		# Get signal return 
		pulse_start_time = 0
		while(GPIO.input(self.pinEcho)==0):
			pulse_start_time = time.time()
		while(GPIO.input(self.pinEcho)==1):
			pulse_end_time = time.time()

		# Calculate distance
		pulse_duration = pulse_end_time - pulse_start_time
		self.distance = round(pulse_duration * 17150, 2)

	def run(self):
		GPIO.setup(self.pinTrig, GPIO.OUT)
		GPIO.setup(self.pinEcho, GPIO.IN)
		GPIO.output(self.pinTrig, GPIO.LOW)

		while not self.isKilled:
			self.update()
			time.sleep(self.intervalTime)

		print(self, " is killed")
	
	def stop(self):
		self.isKilled = True

	def getDistance(self):
		return self.distance