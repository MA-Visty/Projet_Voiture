#!/usr/bin/env python3
#coding:utf−8
__author__ = "KOUATCHE TCHADIO Anila Keren , KOUPTCHINSKY Nicolas , LASSOIS Patrick , Mahieu Alexandre , VINETOT Nathan "
__copyright__ = " Copyright 2023 , HEH - Project Voiture "

from ina219 import INA219
from ina219 import DeviceRangeError
import time

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

		self.ina = INA219(0.1)
		#self.ina.configure() # -> bug motorDC is on

		self.reset()

	def update(self):
		if(self.minPulse <= self.position <= self.maxPulse):
			self.pwm.write(0, 0, self.position)
			self.read()
		else:
			self.reset()
	
	def setPosition(self, _pos):
		if(self.minPulse <= _pos <= self.maxPulse):
			self.position = _pos
	
	def getPosition(self):
		return self.position

	def reset(self):
		self.setPosition(self.midPulse)
		self.update()

	def read(self):
		try:
			pass
			"""
			print("Bus Voltage: %.3f V" % self.ina.voltage())
			print("Bus Current: %.3f mA" % self.ina.current())
			print("Power: %.3f mW" % self.ina.power())
			print("Shunt voltage: %.3f mV" % self.ina.shunt_voltage())
			"""
		except DeviceRangeError as e:
			# Current out of device range with specified shunt resistor
			print(e)