#!/usr/bin/env python3
#coding:utf−8
__author__ = "KOUATCHE TCHADIO Anila Keren , KOUPTCHINSKY Nicolas , LASSOIS Patrick , Mahieu Alexandre , VINETOT Nathan "
__copyright__ = " Copyright 2023 , HEH - Project Voiture "

from ina219 import INA219
from ina219 import DeviceRangeError
from threading import Thread
import time

class INA(Thread):
	def __init__(self, _servo):
		super().__init__()
		self.isKilled = False

		self.servo = _servo

		self.SHUNT_OHMS = 0.1
		self.ina = INA219(self.SHUNT_OHMS)
		self.ina.configure()
	
	def run(self):
		while not self.isKilled:
			try:
				self.getVoltage()
				self.getCurrent()
				self.getPower()
				self.getShuntVoltage()
			except DeviceRangeError as e:
				# Current out of device range with specified shunt resistor
				if(self.servo.getPosition() < self.servo.midPulse):
					self.servo.setPosition(self.servo.getPosition() + 25)
				elif(self.servo.getPosition() > self.servo.midPulse):
					self.servo.setPosition(self.servo.getPosition() - 25)

		print(self, " is killed")
	
	def getVoltage(self):
		return self.ina.voltage()
	
	def getCurrent(self):
		return self.ina.current()
	
	def getPower(self):
		return self.ina.power()
	
	def getShuntVoltage(self):
		return self.ina.shunt_voltage()
	
	def stop(self):
		self.isKilled = True
		self.join()