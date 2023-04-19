import os
import time
from mClass.tuture import Car

def showSpeed(car):
	car.direction.position = car.direction.midPulse
	car.direction.update()
	time.sleep(1)
	car.move(30)
	time.sleep(1)
	car.move(60)
	time.sleep(1)
	car.move(100)
	time.sleep(1)
	car.move(-100)
	time.sleep(1)
	car.move(-60)
	time.sleep(1)
	car.move(-30)
	time.sleep(1)
	car.move(0)

def circule(car):
	speed = 60
	mtime = 5

	car.direction.position = car.direction.maxPulse
	car.direction.update()
	time.sleep(0.5)
	car.move(speed)
	time.sleep(mtime)
	car.move(0)
	time.sleep(0.5)
	car.direction.position = car.direction.midPulse
	car.direction.update()
	time.sleep(0.5)
	car.direction.position = car.direction.minPulse
	car.direction.update()
	time.sleep(0.5)
	car.move(speed)
	time.sleep(mtime)
	car.move(0)
	time.sleep(0.5)

def direction(car):
	car.direction.position = car.direction.maxPulse
	car.direction.update()
	time.sleep(0.5)
	car.direction.position = car.direction.midPulse
	car.direction.update()
	time.sleep(0.5)
	car.direction.position = car.direction.minPulse
	car.direction.update()
	time.sleep(0.5)
	car.direction.position = car.direction.midPulse
	car.direction.update()
	time.sleep(0.5)

if __name__ == "__main__":
	try:
		tuture = Car()
		tuture.start()

		if(int(input("Presentation vitesse (1 => pour oui):")) == 1):
			showSpeed(tuture)
		if(int(input("Presentation cercle (1 => pour oui):")) == 1):
			circule(tuture)
		if(int(input("Presentation direction (1 => pour oui):")) == 1):
			direction(tuture)
			if(int(input("Presentation direction (1 => pour oui):")) == 1):
				while True:
					tuture.direction.position = int(input())
					tuture.direction.update()
					time.sleep(0.5)

		while True:
			os.system("clear")

			print(tuture.sL.getDistance(), "cm | ", tuture.sF.getDistance(), "cm | ", tuture.sR.getDistance(), "cm")
			print("Valeur Infrarouge:", tuture.sI.getValue())
			print("Vitesse moteur Gauche:", tuture.mL.getSpeed())
			print("Vitesse moteur Droit:", tuture.mR.getSpeed())
			print("Position servomoteur:", tuture.direction.getPosition())

			time.sleep(0.1)
	
	except Exception as e:
		pass
	
	finally:
		tuture.stop()