import RPi.GPIO as GPIO

class DC:
	def __init__(self, _in1, _in2, _in3, _in4,_en):
		self.in1=_in1
		self.in2=_in2
		self.in3=_in3
		self.in4=_in4
		self.en=_en
		GPIO.setup(self.in1,GPIO.OUT)
		GPIO.setup(self.in2,GPIO.OUT)
		GPIO.setup(self.in3,GPIO.OUT)
		GPIO.setup(self.in4,GPIO.OUT)
		GPIO.setup(self.en,GPIO.OUT)
		GPIO.output(self.in1,GPIO.LOW)
		GPIO.output(self.in2,GPIO.LOW)
		GPIO.output(self.in3,GPIO.LOW)
		GPIO.output(self.in4,GPIO.LOW)
		self.p=GPIO.PWM(self.en,1000)
		self.p.start(25)
	def forward(self):
		GPIO.output(self.in1,GPIO.HIGH)
		GPIO.output(self.in2,GPIO.LOW)
		GPIO.output(self.in3,GPIO.HIGH)
		GPIO.output(self.in4,GPIO.LOW)
	def backward(self):
		GPIO.output(self.in1,GPIO.LOW)
		GPIO.output(self.in2,GPIO.HIGH)
		GPIO.output(self.in3,GPIO.LOW)
		GPIO.output(self.in4,GPIO.HIGH)
	def stop(self):
		GPIO.output(self.in1,GPIO.LOW)
		GPIO.output(self.in2,GPIO.LOW)
		GPIO.output(self.in3,GPIO.LOW)
		GPIO.output(self.in4,GPIO.LOW)
	def low(self):
		self.p.ChangeDutyCycle(25)
	def medium(self):
		self.p.ChangeDutyCycle(50)
	def high(self):
		self.p.ChangeDutyCycle(75)