import RPi.GPIO as GPIO
import mClass.PCA9685 as p
import time    # Import necessary modules

class DC:
	def __init__(self, _pinA, _pinB, _en):
		self.pinA=_pinA
		self.pinB=_pinB
		self.en=_en
		self.pins=[_pinA,_pinB]
		busnum=None
		
		
		global pwm
		if busnum == None:
			pwm = p.PWM()                  # Initialize the servo controller.
		else:
			pwm = p.PWM(bus_number=busnum) # Initialize the servo controller.
		pwm.frequency = 60
		self.forwardB = 'True'
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BCM)        # Number GPIOs by its physical location
		try:
			for line in open("config"):
				if line[0:8] == "forward0":
					self.forwardB = line[11:-1]
		except:
			pass
		if self.forwardB == 'True':
			self.backwardB = 'False'
		elif self.forwardB == 'False':
			self.backwardB = 'True'
		for pin in self.pins:
			GPIO.setup(pin, GPIO.OUT)   # Set all pins' mode as output
	def motor(self,x):
		if x == 'True':
			GPIO.output(self.pinA, GPIO.LOW)
			GPIO.output(self.pinB, GPIO.HIGH)
		elif x == 'False':
			GPIO.output(self.pinA, GPIO.HIGH)
			GPIO.output(self.pinB, GPIO.LOW)
		else:
			print ('Config Error')
	def setSpeed(self,speed):
		speed *= 40
		print ('speed is: ', speed)
		pwm.write(self.en, 0, speed)
	def backward(self):
		self.motor(self.forwardB)
	def forward(self):
		self.motor(self.backwardB)
	def stop(self):
		for pin in self.pins:
			GPIO.output(pin, GPIO.LOW)