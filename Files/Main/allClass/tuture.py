#!/usr/bin/env python3
#coding:utf−8
__author__ = "KOUATCHE TCHADIO Anila Keren , KOUPTCHINSKY Nicolas , LASSOIS Patrick , Mahieu Alexandre , VINETOT Nathan "
__copyright__ = " Copyright 2023 , HEH - Project Voiture "

import RPi.GPIO as GPIO
import time

from allClass.motors.motorDC import DC
from allClass.motors.servoMotor import PAPA
from allClass.sensors.Color import Color
from allClass.sensors.Infrared import Infrared
from allClass.sensors.UltraSonic import UltraSonic

class Car:
	def __init__(self):
		# Number GPIOs by its physical location
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)

		# Servomotor
		self.direction = PAPA()
		# Motor Left
		self.mL = DC(24, 23, 5)
		# Motor Right
		self.mR = DC(27, 22, 4)

		# Sensor "UltraSonic" Left
		self.sL = UltraSonic(11, 9)
		# Sensor "UltraSonic" Front
		self.sF = UltraSonic(6, 5)
		# Sensor "UltraSonic" Right
		self.sR = UltraSonic(26, 19)

		# Sensor "Infrared"
		self.sI = Infrared(20)
		
		# Sensor "Color"
		self.sC = Color()
	
	def move(self, speed):
		if(100 >= speed >= 10):
			self.mL.forward()
			self.mL.setSpeed(speed)
			self.mR.forward()
			self.mR.setSpeed(speed)
		elif(-100 <= speed <= -10):
			self.mL.backward()
			self.mL.setSpeed(abs(speed))
			self.mR.backward()
			self.mR.setSpeed(abs(speed))
		else:
			self.mL.setSpeed(0)
			self.mR.setSpeed(0)

	def turn(self, deg):
		if(self.direction.minPulse <= deg <= self.direction.maxPulse):
			self.direction.setPosition(deg)
	
	def start(self):
		self.sL.start()
		self.sF.start()
		self.sR.start()
		self.sI.start()
		self.sC.start()

		self.direction.start()
		self.direction.reset()
		self.move(0)
	
	def stop(self):
		self.mL.stop()
		self.mR.stop()
		self.direction.stop()
		self.direction.reset()
		self.sL.stop()
		self.sF.stop()
		self.sR.stop()
		self.sI.stop()
		self.sC.stop()
		GPIO.cleanup()