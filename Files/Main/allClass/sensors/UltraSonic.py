#!/usr/bin/env python3
#coding:utf−8
__author__ = "KOUATCHE TCHADIO Anila Keren , KOUPTCHINSKY Nicolas , LASSOIS Patrick , Mahieu Alexandre , VINETOT Nathan "
__copyright__ = " Copyright 2023 , HEH - Project Voiture "

import RPi.GPIO as GPIO
import time

from allClass.sensors.Sensors import Sensor

class UltraSonic(Sensor):
	def __init__(self, _pinTrig, _pinEcho):
		super().__init__()
		self.pinTrig = _pinTrig
		self.pinEcho = _pinEcho
		self.distance = 0
		self.distances = []

		# Set up the GPIO pins
		GPIO.setup(self.pinTrig, GPIO.OUT)
		GPIO.setup(self.pinEcho, GPIO.IN)

	def run(self):
		GPIO.output(self.pinTrig, GPIO.LOW)

		while not self.isKilled:
			# Send signal
			GPIO.output(self.pinTrig, GPIO.HIGH)
			time.sleep(0.00001)
			GPIO.output(self.pinTrig, GPIO.LOW)

			# Get signal return 
			pulse_start_time = 0
			while(GPIO.input(self.pinEcho)==0):
				pulse_start_time = time.time()
			while(GPIO.input(self.pinEcho)==1):
				pulse_end_time = time.time()

			# Calculate distance
			pulse_duration = pulse_end_time - pulse_start_time
			self.setDistance(round(pulse_duration * 17150, 2))

		print(self, " is killed")

	def setDistance(self, _distance):
		if(2 <= _distance <= 400):
			if(len(self.distances) == 0):
				self.distance = _distance
				self.distances.append(self.distance)
			else:
				moyenne = 0
				for nbr in self.distances:
					moyenne += nbr
				moyenne = moyenne / len(self.distances)

				if((moyenne - (moyenne * 0.1)) < _distance < (moyenne + (moyenne * 0.1))):
					self.distances.append(_distance)
					self.distance = _distance

				if(len(self.distances) > 5):
					self.distances.pop(0)
	
	def getDistance(self):
		return self.distance