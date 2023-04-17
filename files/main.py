from mClass.tuture import Car

if __name__ == "__main__":
	tuture = Car()

	while True:
		tuture.sL.getDistance()
		tuture.sF.getDistance()
		tuture.sR.getDistance()

		tuture.sI.getInfo()