from mClass.PCA9685 import PWM
import time

class PAPA:
	def __init__(self):
		self.minPulse = 150
		self.midPulse = 250
		self.maxPulse = 450
		self.position = 0
		self.frequency = 50
		self.pwm = PWM()
		self.pwm.frequency = self.frequency

		self.reset()

	def turn(self, left=False, right=False):
		if(left):
			self.position += 15
		if(right):
			self.position -= 15
		
		if(self.position < self.minPulse):
			self.position = self.minPulse
		if(self.position > self.maxPulse):
			self.position = self.maxPulse

		self.update()

	def update(self):
		self.pwm.write(0, 0, self.position)

	def reset(self):
		self.position = self.midPulse
		self.update()