from mClass.PCA9685 import PWM
import time
from ina219 import INA219
from ina219 import DeviceRangeError

class PAPA:
	def __init__(self):
		self.minPulse = 150
		self.midPulse = 250
		self.maxPulse = 400
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
		self.read()
	
	def setPosition(self, _pos):
		self.position = _pos
	
	def getPosition(self):
		self.read()
		return self.position

	def reset(self):
		self.position = self.midPulse
		self.update()

	def read(self):
		ina = INA219(0.1)
		"""
		ina.configure()
		print("Bus Voltage: %.3f V" % ina.voltage())
		try:
			print("Bus Current: %.3f mA" % ina.current())
			print("Power: %.3f mW" % ina.power())
			print("Shunt voltage: %.3f mV" % ina.shunt_voltage())
		except DeviceRangeError as e:
			# Current out of device range with specified shunt resistor
			print(e)
		"""