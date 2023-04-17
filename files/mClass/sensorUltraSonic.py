import RPi.GPIO as GPIO
import time

class UltraSonic:
	def __init__(self, _pinTrig, _pinEcho, _intervalTime=1):
		self.pinTrig = _pinTrig
		self.pinEcho = _pinEcho

		self.intervalTime = _intervalTime
		self.mThread = Thread(target=self.getDistance, args=[])

	def getDistance(self):
		GPIO.setup(self.pinTrig, GPIO.OUT)
		GPIO.setup(self.pinEcho, GPIO.IN)
		GPIO.output(self.pinTrig, GPIO.LOW)

		while True:
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