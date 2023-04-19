import os
import time
import keyboard
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

def controleDistance(car):
	first = time.time()
	while True:
		if keyboard.is_pressed('q'):
			if(time.time() - first >= 0.2):
				first = time.time()
				if(car.direction.position == car.direction.maxPulse):
					car.direction.position = car.direction.midPulse
					car.direction.update()
				elif(car.direction.position == car.direction.midPulse):
					car.direction.position = car.direction.minPulse
					car.direction.update()
				else:
					pass
		if keyboard.is_pressed('z'):
			if(time.time() - first >= 0.2):
				first = time.time()
				print('z')
		if keyboard.is_pressed('s'):
			if(time.time() - first >= 0.2):
				first = time.time()
				print('s')
		if keyboard.is_pressed('d'):
			if(time.time() - first >= 0.2):
				first = time.time()
				if(car.direction.position == car.direction.minPulse):
					car.direction.position = car.direction.midPulse
					car.direction.update()
				elif(car.direction.position == car.direction.midPulse):
					car.direction.position = car.direction.maxPulse
					car.direction.update()
				else:
					pass

if __name__ == "__main__":
	try:
		tuture = Car()
		tuture.start()
		compteur=0
		while 1:
			print(compteur)
			if(tuture.sI.getValue==1):
				compteur+=1
		time.sleep(0.1)
	except Exception as e:
		print(e)
	
	finally:
		tuture.stop()