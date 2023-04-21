#!/usr/bin/env python3
#coding:utf−8
__author__ = "KOUATCHE TCHADIO Anila Keren , KOUPTCHINSKY Nicolas , LASSOIS Patrick , Mahieu Alexandre , VINETOT Nathan "
__copyright__ = " Copyright 2023 , HEH - Project Voiture "

import keyboard
import os
import random
import time

from allClass.tuture import Car

# Fait avancer la voiture avec différentes vitesses
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

# Fait tourner les roues des deux côtés
def showDirection(car):
	car.turn(car.direction.maxPulse)
	time.sleep(0.5)
	car.turn(car.direction.midPulse)
	time.sleep(0.5)
	car.turn(car.direction.minPulse)
	time.sleep(0.5)
	car.turn(car.direction.midPulse)
	time.sleep(0.5)

# Fait faire un cercle avec la voiture puis le reproduit dans l'autre sens
def showCircle(car):
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

# Fait suivre le mur droit à la voiture
def suivimur(car):
	car.move(30)

	while True:
		if(car.sF.getDistance()<40):
			break

		srDistance=car.sR.getDistance()
		slDistance=car.sL.getDistance()
		if(slDistance<srDistance):
			dist=slDistance*1.5
			if(15< slDistance < 18):
				car.turn(250)
			elif(slDistance < 15):
				car.turn(250+dist)
			elif(slDistance > 18):
				car.turn(250-dist)
		if(srDistance<slDistance):
			if(15< srDistance < 18):
				car.turn(250)
			elif(srDistance < 15):
				car.turn(250+dist)
			elif(srDistance > 18):
				car.turn(250-dist)

# Éviter l'obstacle devant la voiture
def eviteObj(car):
	while True:
		if(car.sF.getDistance()>35):
			if(car.sR.getDistance()<25):
				car.turn(180)
				car.move(30)
			elif(car.sL.getDistance()<25):
				car.turn(340)
				car.move(30)
			else:
				car.move(0)
				car.turn(250)

# Fait faire le circuit à la voiture
def circuitTour(car):
	car.move(30)
	while True:
		if(car.sF.getDistance()>35):
			if(car.sR.getDistance()<25):
				car.turn(180)
			elif(car.sL.getDistance()<25):
				car.turn(340)
			else:
				car.turn(250)
		elif(car.sR.getDistance()>car.sL.getDistance()):
			car.turn(400)
			time.sleep(1)
		else:
			car.turn(150)
			time.sleep(1)

# Fait faire un certain nombre de tour(s) à la voiture
def circuitNbrTour(car):
	nbtour=int(input("Combien de tours ? "))
	car.sI.reset(nbtour)
	while not car.sI.valueStop:
		circuitTour(car)

# Fait faire un nombre aléatoire de tour à la voiture
def circuitNbrRandomTour(car):
	nbtour = random.randint(1, 5)
	car.sI.reset(nbtour)
	while not car.sI.valueStop:
		circuitTour(car)

# Fait faire le circuit à la voiture quand le feu passe au vert
def circuitTourColor(car):
	while not car.sC.getGO():
		pass

	while True:
			if(car.sF.getDistance()>35):
				if(car.sR.getDistance()<25):
					car.turn(180)
				elif(car.sL.getDistance()<25):
					car.turn(340)
				else:
					car.turn(250)
			elif(car.sR.getDistance()>car.sL.getDistance()):
				car.turn(400)
				time.sleep(1)
			else:
				car.turn(150)
				time.sleep(1)

# Permets de tester différentes vitesses aux moteurs
def testSpeed(car):
	while True:
		clear()
		print("Vitesse moteur gauche actuelle : ", car.mL.getSpeed())
		print("Vitesse moteur droit actuelle : ", car.mR.getSpeed())
		car.move(int(input("Valeur : ")))

# Permets de tester différents angle au servo-moteur ( roues )
def testDirection(car):
	while True:
		clear()
		printINA(car)
		print("Position actuelle : ", car.direction.getPosition())
		car.turn(int(input("Valeur : ")))

# Permets de faire tourner sur elle-même (faire Burn) la voiture
def testChar(car, left=False, right=False, time=0.0):
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

# Donne les informations de la voiture + les informations du capteur de couleur
def testColor(car):
	while True:
		printInfo(car)
		print()
		print(car.sC.valColor)
		print(car.sC.valLux)
		print(car.sC.getGO())
		if(car.sC.getGO()):
			car.move(30)
			
# Permets de contrôler la voiture à distance (un peu compliquer)
def testControle(car):
	speed = 0
	while True:
		nbr = input("z | q | s | d >>> ")

		if(nbr == "z"):
			if(speed < 0):
				car.move(0)
				speed = 0
			else:
				car.move(60)
				speed = 60
		elif(nbr == "s"):
			if(speed > 0):
				car.move(0)
				speed = 0
			else:
				car.move(-60)
				speed = -60
		elif(nbr == "q"):
			if(car.direction.getPosition() > 250):
				car.turn(245)
			else:
				car.turn(150)
		elif(nbr == "d"):
			if(car.direction.getPosition() < 250):
				car.turn(255)
			else:
				car.turn(400)

# Efface la console
def clear():
	os.system("clear")

# Affiche les informations des différents capteurs (Ultrason, Infrarouge, Couleur, Vitesse des moteurs, Position des servo-moteurs)
def printInfo(car):
	clear()
	print(car.sL.getDistance(), "cm | ", car.sF.getDistance(), "cm | ", car.sR.getDistance(), "cm")
	print("Valeur Infrarouge:", car.sI.getValue())
	print('Valeur Couleur: ', car.sC.getColor())
	print('Valeur Temperature:', car.sC.getTemp(), 'K')
	print('Valeur Lux:', car.sC.getLux())
	print("Vitesse moteur Gauche:", car.mL.getSpeed())
	print("Vitesse moteur Droit:", car.mR.getSpeed())
	print("Position servomoteur:", car.direction.getPosition())
	printINA(car)

# Affiche les informations du limiteur de courant
def printINA(car):
	print("Bus Voltage: %.3f V" % car.direction.ina.getVoltage())
	print("Bus Current: %.3f mA" % car.direction.ina.getCurrent())
	print("Power: %.3f mW" % car.direction.ina.getPower())
	print("Shunt voltage: %.3f mV" % car.direction.ina.getShuntVoltage())

# Affiche un menu
def menu(car):
	try:
		clear()
		print("> ",  ('-'*12), " Menu ", ('-'*12))
		print(" Info General - 		 1")
		print(" Presentation Vitesse - 	 2")
		print(" Presentation Direction - 	 3")
		print(" Presentation Cercle - 		 4")
		print(" Longer mur - 			 5")
		print(" Eviter obstacle - 		 6")
		print(" Circuit - 			 7")
		print(" Circuit n° tour - 		 8")
		print(" Circuit n°? tour - 		 9")
		print(" Circuit feux - 		10")
		print("> ", ('-'*32))
		print(" Test Vitesse - 		11")
		print(" Test Direction - 		12")
		print(" Test Char - 			13")
		print(" Test Capteur Couleur - 	14")
		print(" Test Controle Distance - 	15")
		print("> ", ('-'*32))
		print(" Exit - 			 0")
		print("< ", ('-'*32))
		
		choix = int(input(">>> "))
		if(choix == 0):
			exit()
		elif(choix == 1):
			while True:
				printInfo(car)
				time.sleep(0.5)
		elif(choix == 2):
			showSpeed(car)
		elif(choix == 3):
			showDirection(car)
		elif(choix == 4):
			showCircle(car)
		elif(choix == 5):
			suivimur(car)
		elif(choix == 6):
			eviteObj(car)
		elif(choix == 7):
			circuitTour(car)
		elif(choix == 8):
			circuitNbrTour(car)
		elif(choix == 9):
			circuitNbrRandomTour(car)
		elif(choix == 10):
			circuitTourColor(car)
		elif(choix == 11):
			testSpeed(car)
		elif(choix == 12):
			testDirection(car)
		elif(choix == 13):
			car.turn(150)
			testChar(car, left=True, time=0.5)
			car.turn(350)
			testChar(car, right=True, time=0.5)
		elif(choix == 14):
			testColor(car)
		elif(choix == 15):
			testControle(car)
					
	except Exception as e:
		print(e)
		input("Presse <<ENTER>> pour passer l'erreur")
		menu(car)

if __name__ == "__main__":
	try:
		# Initialise une voiture
		tuture = Car()
		tuture.start()

		while True:
			menu(tuture)
			

	except Exception as e:
		print(e)
	
	finally:
		# Stop les différents composants de la voiture
		tuture.stop()