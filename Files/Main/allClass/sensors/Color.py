#!/usr/bin/env python3
#coding:utf−8
__author__ = "KOUATCHE TCHADIO Anila Keren , KOUPTCHINSKY Nicolas , LASSOIS Patrick , Mahieu Alexandre , VINETOT Nathan "
__copyright__ = " Copyright 2023 , HEH - Project Voiture "

import RPi.GPIO as GPIO
import time

from allClass.sensors.Sensors import Sensor

class Color(Sensor):
	def __init__(self):
		super().__init__()

	def run(self):
		print(self, " is killed")