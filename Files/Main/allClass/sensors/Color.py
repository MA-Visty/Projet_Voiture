#!/usr/bin/env python3
#coding:utf−8
__author__ = "KOUATCHE TCHADIO Anila Keren , KOUPTCHINSKY Nicolas , LASSOIS Patrick , Mahieu Alexandre , VINETOT Nathan "
__copyright__ = " Copyright 2023 , HEH - Project Voiture "

import RPi.GPIO as GPIO
import time
import board
import adafruit_tcs34725

from allClass.sensors.Sensors import Sensor

class Color(Sensor):
	def __init__(self):
		super().__init__()
		self.i2c = board.I2C()
		self.sensor = adafruit_tcs34725.TCS34725(self.i2c)

		self.colors = []
		self.valColor = 0
		self.valTemp = 0
		self.valLux = 0
		self.tTime = None
		self.valStart = False

	def run(self):
		while not self.isKilled:
			self.setColor(self.sensor.color_rgb_bytes)
			self.setTemp(self.sensor.color_temperature)
			self.setLux(self.sensor.lux)

		print(self, " is killed")

	def getGO(self):
		return self.valStart
	
	def setColor(self, _valC):
		if(len(self.colors) == 0):
			if(_valC[1] > _valC[0] and _valC[0] > _valC[2]):
				self.valStart = True
			else:
				self.valStart = False
			
			self.valColor = _valC
			self.colors.append(_valC)
		else:
			moyenneR = 0
			moyenneG = 0
			moyenneB = 0
			for nbr in self.colors:
				moyenneR += nbr[0]
				moyenneG += nbr[1]
				moyenneB += nbr[2]
			moyenneR = moyenneR / len(self.colors)
			moyenneG = moyenneG / len(self.colors)
			moyenneB = moyenneB / len(self.colors)

			if((moyenneG - (moyenneG * 0.1)) < _valC[1] < (moyenneG + (moyenneG * 0.1))):
				if(_valC[1] > _valC[0] and _valC[1] > _valC[2]):
					self.valStart = True
				else:
					self.valStart = False
			
			self.valColor = _valC
			self.colors.append(_valC)

			if(len(self.colors) > 5):
				self.colors.pop(0)

	def getColor(self):
		return self.valColor
	
	def setTemp(self, _valT):
		self.valTemp = _valT

	def getTemp(self):
		return self.valTemp
	
	def setLux(self, _valL):
		self.valLux = _valL

	def getLux(self):
		return self.valLux