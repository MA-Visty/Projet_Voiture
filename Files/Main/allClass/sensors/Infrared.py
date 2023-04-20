#!/usr/bin/env python3
#coding:utf−8
__author__ = "KOUATCHE TCHADIO Anila Keren , KOUPTCHINSKY Nicolas , LASSOIS Patrick , Mahieu Alexandre , VINETOT Nathan "
__copyright__ = " Copyright 2023 , HEH - Project Voiture "

import RPi.GPIO as GPIO
import time

from allClass.sensors.Sensors import Sensor

class Infrared(Sensor):
	def __init__(self, _pin):
		super().__init__()
		self.pin = _pin
		self.value = 0
	
	def run(self):
		# Set up the GPIO pins
		GPIO.setup(self.pin, GPIO.IN)

		while not self.isKilled:
			self.setValue(GPIO.input(self.pin))
			time.sleep(0.1)

		print(self, " is killed")

	def setValue(self, _val):
		self.value = _val

	def getValue(self):
		return self.value