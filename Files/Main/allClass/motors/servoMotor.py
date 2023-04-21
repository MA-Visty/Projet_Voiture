#!/usr/bin/env python3
#coding:utf−8
__author__ = "KOUATCHE TCHADIO Anila Keren , KOUPTCHINSKY Nicolas , LASSOIS Patrick , Mahieu Alexandre , VINETOT Nathan "
__copyright__ = " Copyright 2023 , HEH - Project Voiture "

from allClass.motors.PCA9685 import PWM
from allClass.motors.limiteurINA import INA

class PAPA:
	def __init__(self):
		self.minPulse = 150
		self.midPulse = 300
		self.maxPulse = 400
		self.position = self.midPulse
		self.frequency = 50

		self.pwm = PWM()
		self.pwm.frequency = self.frequency

		self.ina = INA(self)

	def update(self):
		if(self.minPulse <= self.position <= self.maxPulse):
			self.pwm.write(0, 0, self.position)
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
	
	def start(self):
		self.ina.start()
	
	def stop(self):
		self.ina.stop()