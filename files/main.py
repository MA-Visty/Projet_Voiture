import RPi.GPIO as GPIO

from mClass.tuture import Car

if __name__ == "__main__":
	tuture = Car()
	tuture.start()