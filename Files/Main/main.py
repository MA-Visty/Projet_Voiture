#!/usr/bin/env python3
#coding:utf−8
__author__ = "KOUATCHE TCHADIO Anila Keren , KOUPTCHINSKY Nicolas , LASSOIS Patrick , Mahieu Alexandre , VINETOT Nathan "
__copyright__ = " Copyright 2023 , HEH - Project Voiture "

import keyboard
import os
import time

from allClass.tuture import Car

def showSpeed(car):
	car.turn(car.direction.midPulse)
	time.sleep(1)

	for i in range(4):
		car.move(25 * i)
		time.sleep(1)
	
	for i in range(4):
		car.move(100 - (25 * i))
		time.sleep(1)
	
	car.move(0)

def circule(car):
	speed = 60
	mtime = 5

	car.turn(car.direction.maxPulse)
	time.sleep(0.5)
	car.move(speed)
	time.sleep(mtime)
	car.move(0)
	time.sleep(0.5)
	car.turn(car.direction.midPulse)
	time.sleep(0.5)
	car.turn(car.direction.minPulse)
	time.sleep(0.5)
	car.move(speed)
	time.sleep(mtime)
	car.move(0)
	time.sleep(0.5)

def direction(car):
	car.turn(car.direction.maxPulse)
	time.sleep(0.5)
	car.turn(car.direction.midPulse)
	time.sleep(0.5)
	car.turn(car.direction.minPulse)
	time.sleep(0.5)
	car.turn(car.direction.midPulse)
	time.sleep(0.5)

def testAlgo(car):
	while True:
		printInfo(car)

		if(car.sF.getDistance() >= 20):
			car.move(100)
		else:
			car.move(0)

		if(car.sL.getDistance() < 30):
			car.turn(200)
		else:
			car.turn(255)
		if(car.sL.getDistance() > 40):
			car.turn(300)
		else:
			car.turn(245)
		"""
		if(car.sL.getDistance() < 25):
			car.turn(350)
		else:
			car.turn(250)
		if(car.sR.getDistance() < 25):
			car.turn(150)
		else:
			car.turn(250)
		"""
		
		time.sleep(0.05)

def printInfo(car):
	os.system("clear")
	print(car.sL.getDistance(), "cm | ", car.sF.getDistance(), "cm | ", car.sR.getDistance(), "cm")
	print("Valeur Infrarouge:", car.sI.getValue())
	print("Valeur Couleur:", "none")
	print("Vitesse moteur Gauche:", car.mL.getSpeed())
	print("Vitesse moteur Droit:", car.mR.getSpeed())
	print("Position servomoteur:", car.direction.getPosition())

def char(car, left=False, right=False, time=0.0):
	if(left):
		car.mL.backward()
		car.mL.setSpeed(100)
		car.mR.forward()
		car.mR.setSpeed(100)
		time.sleep(time)
		car.move(0)
	
	if(right):
		car.mL.forward()
		car.mL.setSpeed(100)
		car.mR.backward()
		car.mR.setSpeed(100)
		time.sleep(time)
		car.move(0)

def menu(car):
	try:
		print("> ------")
		print("Info General - 1")
		print("Presentation Vitesse - 2")
		print("Presentation Direction - 3")
		print("Presentation Cercle - 4")
		print("> ------")
		print("Controle a Distance - ")
		print("Test Direction - 6")

		print("Test Algo - 7")
		print("Char - 8")
		
		choix = int(input(">>> "))
		
		if(choix == 1):
			while True:
				printInfo(car)
				time.sleep(0.5)
		elif(choix == 2):
			showSpeed(car)
		elif(choix == 3):
			direction(car)
		elif(choix == 4):
			circule(car)
		elif(choix == 5):
			pass
		elif(choix == 6):
			while True:
				car.turn(int(input("Valeur : ")))
				time.sleep(0.5)
		elif(choix == 7):
			testAlgo(car)
		elif(choix == 8):
			car.turn(150)
			char(car, left=True, time=0.5)
			car.turn(350)
			char(car, right=True, time=0.5)
	except Exception as e:
		print(e)
		input("Press <<ENTER>> for pass error")
		menu(car)
def suivimur(car):
	if(car.sR.getDistance()<22):
		car.turn(180)
	elif(car.sR.getDistance()>23):
		car.turn(320)
	else:
		car.turn(250)
if __name__ == "__main__":
	try:
		tuture = Car()
		tuture.start()
		
		while True:
			suivimur()
	except Exception as e:
		print(e)
	
	finally:
		tuture.stop()