from Motors import *
from Sensors import *

class Car:
	def __init__(self):
		# Motor Left
		self.mL = DC()
		# Motor Right
		self.mR = DC()
		# Servo Motor
		self.direction = PAPA()

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

if __name__ == "__main__":
	print("v2")
	print()
	tuture = Car()

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