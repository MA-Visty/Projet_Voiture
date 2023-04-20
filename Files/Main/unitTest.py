import time
import unittest
import RPi.GPIO as GPIO

from allClass.motors.motorDC import DC
from allClass.motors.servoMotor import PAPA
from allClass.sensors.Color import Color
from allClass.sensors.Infrared import Infrared
from allClass.sensors.Sensors import Sensor
from allClass.sensors.UltraSonic import UltraSonic
from allClass.tuture import Car

class testMotorDC(unittest.TestCase):

	def setUp(self):
		print("--- Test MotorDC ---")
		# Motor
		self.m = DC(24, 23, 5)

	def tearDown(self):
		print("--- Fin du Test ---")

	def test_simple(self):
		self.assertTrue(True)

class testServoMotor(unittest.TestCase):

	def setUp(self):
		print("--- Test ServoMotor ---")
		# Servomotor
		self.direction = PAPA()

	def tearDown(self):
		print("--- Fin du Test ---")

	def test_simple(self):
		self.assertTrue(True)

class testSensors(unittest.TestCase):

	def setUp(self):
		print("--- Test Sensors ---")
		# Sensor
		self.sS = Sensor()

	def tearDown(self):
		print("--- Fin du Test ---")

	def test_simple(self):
		self.assertTrue(True)

class testColor(unittest.TestCase):

	def setUp(self):
		print("--- Test Color ---")
		# Sensor "Color"
		self.sC = Color()

	def tearDown(self):
		print("--- Fin du Test ---")

	def test_simple(self):
		self.assertTrue(True)

class testUlraSonic(unittest.TestCase):

	def setUp(self):
		print("--- Test UltraSonic ---")
		# Sensor "UltraSonic"
		self.sU = UltraSonic(11, 9)
		self.sU.start()

	def tearDown(self):
		print("--- Fin du Test ---")

	def test_simple(self):
		self.assertTrue(True)
		time.sleep(1)
		print(self.sU.getDistance())
		
class testInfrared(unittest.TestCase):

	def setUp(self):
		print("--- Test Infrared ---")
		# Sensor "Infrared"
		self.sI = Infrared(20)

	def tearDown(self):
		print("--- Fin du Test ---")

	def test_simple(self):
		self.assertTrue(True)
		
if __name__ == '__main__':
	# Number GPIOs by its physical location
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	unittest.main()