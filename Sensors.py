import RPi.GPIO as GPIO
from threading import Thread
import time

class Sensor:
	def __init__(self, _pinTrig, _pinEcho, _intervalTime=1):
		self.pinTrig = _pinTrig
		self.pinEcho = _pinEcho

		self.intervalTime = _intervalTime
		self.mThread = Thread(target=self.getDistance, args=[])

class UltraSonic(Sensor):
	def __init__(self):
		super().__init__()

	def getDistance(self):
		try:
			GPIO.setmode(GPIO.BOARD)
			GPIO.setup(self.pinTrig, GPIO.OUT)
			GPIO.setup(self.pinEcho, GPIO.IN)
			GPIO.output(self.pinTrig, GPIO.LOW)

			while self.run:
				GPIO.output(self.pinTrig, GPIO.HIGH)
				time.sleep(0.00001)
				GPIO.output(self.pinTrig, GPIO.LOW)

				pulse_start_time = 0
				while(GPIO.input(self.pinEcho)==0):
					pulse_start_time = time.time()
				while(GPIO.input(self.pinEcho)==1):
					pulse_end_time = time.time()

				pulse_duration = pulse_end_time - pulse_start_time
				distance = round(pulse_duration * 17150, 2)
				print("Distance:", distance, "cm")

				time.sleep(self.intervalTime)
		finally:
			GPIO.cleanup()

class Color(Sensor):
	def __init__(self):
		super().__init__()

class Infrared(Sensor):
	def __init__(self):
		super().__init__()