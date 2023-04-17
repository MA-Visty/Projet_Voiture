class Sensor:
	def __init__(self):
		print(type(self).__name__)

class UltraSonic(Sensor):
	def __init__(self):
		super().__init__()

class Color(Sensor):
	def __init__(self):
		super().__init__()

class Infrared(Sensor):
	def __init__(self):
		super().__init__()