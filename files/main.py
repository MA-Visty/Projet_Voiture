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
def chackWall(car):
	srDistance=car.sR.getDistance()
	slDistance=car.sL.getDistance()
	if(slDistance<srDistance):
		
		if(30< slDistance < 32):
			tuture.turn(250)
		elif(slDistance < 30):
			print(slDistance)
			tuture.turn(275)
		elif(slDistance > 32):
			tuture.turn(225)
	if(srDistance<slDistance):
		if(30< srDistance < 32):
			tuture.turn(250)
		elif(srDistance < 30):
			tuture.turn(225)
		elif(srDistance > 32):
			tuture.turn(275)

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
def chackWall(car):
	srDistance=car.sR.getDistance()
	slDistance=car.sL.getDistance()
	if(slDistance<srDistance):
		dist=slDistance*1.5
		if(15< slDistance < 18):
			tuture.turn(250)
		elif(slDistance < 15):
			tuture.turn(250+dist)
		elif(slDistance > 18):
			tuture.turn(250-dist)
	if(srDistance<slDistance):
		if(15< srDistance < 18):
			tuture.turn(250)
		elif(srDistance < 15):
			tuture.turn(250+dist)
		elif(srDistance > 18):
			tuture.turn(250-dist)
if __name__ == "__main__":
	try:
		tuture = Car()
		tuture.start()
		tuture.move(30)

		while True:
			os.system("clear")
			if(tuture.sF.getDistance()<40):
				tuture.stop()
				break
			chackWall(tuture)
			time.sleep(0.1)
	except Exception as e:
		print(e)
	
	finally:
		tuture.stop()