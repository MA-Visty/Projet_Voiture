#!/usr/bin/env python3
#coding:utf−8
__author__ = "KOUATCHE TCHADIO Anila Keren , KOUPTCHINSKY Nicolas , LASSOIS Patrick , Mahieu Alexandre , VINETOT Nathan "
__copyright__ = " Copyright 2023 , HEH - Project Voiture "

from threading import Thread

class Sensor(Thread):
	def __init__(self):
		super().__init__()
		self.isKilled = False
	
	def stop(self):
		self.isKilled = True
		self.join()