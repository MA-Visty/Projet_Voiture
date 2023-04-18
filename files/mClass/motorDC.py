from __future__ import division
import RPi.GPIO as GPIO
import Adafruit_PCA9685

class DC:
	def __init__(self, _in1, _in2,_en):
		self.in1=_in1
		self.in2=_in2
		self.pwm=Adafruit_PCA9685.PCA9685()
		self.pwm.set_pwm_freq(60)
		self.en=_en
		self.pwm.set_pwm(_en,4096,0)
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.in1,GPIO.OUT)
		GPIO.setup(self.in2,GPIO.OUT)
		GPIO.output(self.in1,GPIO.LOW)
		GPIO.output(self.in2,GPIO.LOW)
	def forward(self):
		GPIO.output(self.in1,GPIO.HIGH)
		GPIO.output(self.in2,GPIO.LOW)
	def backward(self):
		GPIO.output(self.in1,GPIO.LOW)
		GPIO.output(self.in2,GPIO.HIGH)
	def stop(self):
		GPIO.output(self.in1,GPIO.LOW)
		GPIO.output(self.in2,GPIO.LOW)
	def low(self):
		self.pwm.set_pwm(self.en,1300,0)
	def medium(self):
		self.pwm.set_pwm(self.en,2700,0)
	def high(self):
		self.pwm.set_pwm(self.en,4096,0)
