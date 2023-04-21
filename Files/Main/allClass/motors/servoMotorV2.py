#!/usr/bin/env python3
#coding:utf−8
__author__ = "KOUATCHE TCHADIO Anila Keren , KOUPTCHINSKY Nicolas , LASSOIS Patrick , Mahieu Alexandre , VINETOT Nathan "
__copyright__ = " Copyright 2023 , HEH - Project Voiture "

from ina219 import INA219
from ina219 import DeviceRangeError

from allClass.motors.PCA9685 import PWM

class PAPA:
	def __init__(self):
		self.minPulse = 150
		self.midPulse = 250
		self.maxPulse = 400
		self.position = self.midPulse
		self.frequency = 50

		self.pwm = PWM()
		self.pwm.frequency = self.frequency

		self.SHUNT_OHMS = 0.1
		#self.ina = INA219(self.SHUNT_OHMS)
		#self.ina.configure()

		self.reset()

	def update(self):
		if(self.minPulse <= self.position <= self.maxPulse):
			self.pwm.write(0, 0, self.position)
			#self.read()
		else:
			self.reset()
	
	def setPosition(self, _pos):
		if(self.minPulse <= _pos <= self.maxPulse):
			self.position = _pos
		self.update()
	
	def getPosition(self):
		return self.position

	def reset(self):
		self.setPosition(self.midPulse)

	def read(self):
		pass
		"""
		try:
			if(self.ina.shunt_voltage() > 9):
				if(self.position > self.midPulse):
					self.setPosition(self.position - 25)
				elif(self.position < self.midPulse):
					self.setPosition(self.position + 25)
				else:
					print("Danger servomotor !")
		except DeviceRangeError as e:
			# Current out of device range with specified shunt resistor
			print(e)
		"""
	
	def getVoltage(self):
		return self.ina.voltage()
	
	def getCurrent(self):
		return self.ina.current()
	
	def getPower(self):
		return self.ina.power()
	
	def getShuntVoltage(self):
		return self.ina.shunt_voltage()