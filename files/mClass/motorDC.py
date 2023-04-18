import RPi.GPIO as GPIO
import mClass.PCA9685 as p
import time    # Import necessary modules

class DC:
	def __init__(self, _pina, _pinb, _en):
		self.pina=_pina
		self.pinb=_pinb
		self.en=_en
		self.pins=[_pina,_pinb]
		busnum=None
		global forward, backward
		global pwm
		if busnum == None:
			pwm = p.PWM()                  # Initialize the servo controller.
		else:
			pwm = p.PWM(bus_number=busnum) # Initialize the servo controller.
		pwm.frequency = 60
		forward = 'True'
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BCM)        # Number GPIOs by its physical location
		try:
			for line in open("config"):
				if line[0:8] == "forward0":
					forward = line[11:-1]
		except:
			pass
		if forward == 'True':
			backward = 'False'
		elif forward == 'False':
			backward = 'True'
		for pin in self.pins:
			GPIO.setup(pin, GPIO.OUT)   # Set all pins' mode as output
	def motor(self,x):
		if x == 'True':
			GPIO.output(self.pina, GPIO.LOW)
			GPIO.output(self.pinb, GPIO.HIGH)
		elif x == 'False':
			GPIO.output(self.pina, GPIO.HIGH)
			GPIO.output(self.pinb, GPIO.LOW)
		else:
			print ('Config Error')
	def setSpeed(self,speed):
		speed *= 40
		print ('speed is: ', speed)
		pwm.write(self.en, 0, speed)
	def backward(self):
		self.motor(forward)
	def forward(self):
		self.motor(backward)
	def stop(self):
		for pin in self.pins:
			GPIO.output(pin, GPIO.LOW)
	