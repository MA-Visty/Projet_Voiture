from Motors import *
from Sensors import *

class Car:
	def __init__(self):
		# Motor Left
		self.mL = DC() #19, 18, 17, 16
		# Motor Right
		self.mR = DC()
		# Servo Motor
		self.direction = PAPA() # 23, 22B, 21

		# Sensor "UltraSonic" Left
		self.sL = UltraSonic()
		# Sensor "UltraSonic" Front
		self.sF = UltraSonic()
		# Sensor "UltraSonic" Right
		self.sR = UltraSonic()

		# Sensor "RGB"
		self.sC = Color()
		# Sensor "Infrared"
		self.sI = Infrared()

		#trig 11
		#echo 09

		#trig 6
		#echo 5

		#GPIO.BCM 20

		#trig 26
		#echo 19

if __name__ == "__main__":
	tuture = Car()

	while True:
		#tuture.sL.getDistance()
		pass

	""" TEST -> Multi Thread

	from RandomThread import *

	threads = [RandomThread(str(int_name)) for int_name in range(10)]

	for thread in threads:
		thread.start()

	print("Il y a " + str(threading.activeCount()) + " threads actifs")
	print("Attente de la terminaison des threads")

	for thread in threads:
		thread.join()

	print("Tous les threads sont terminés")
	"""