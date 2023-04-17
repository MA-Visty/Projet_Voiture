import RPi.GPIO as GPIO
import time

class DC:
	def __init__(self, _pin1, _pin2, _pinEN):
		self.pin1 = _pin1
		self.pin2 = _pin2
		self.pinEN = _pinEN

		GPIO.setup(self.pin1,GPIO.OUT)
		GPIO.setup(self.pin2,GPIO.OUT)
		GPIO.setup(self.pinEN,GPIO.OUT)
		
	def test(self):
		GPIO.output(self.pin1,GPIO.LOW)
		GPIO.output(self.pin2,GPIO.LOW)
		p=GPIO.PWM(self.pinEN,1000)
		p.start(25)
		print("\n")
		print("The default speed & direction of motor is LOW & Forward.....")
		print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
		print("\n")    

		while(1):

			x=raw_input()
			
			if x=='r':
				print("run")
				if(temp1==1):
					GPIO.output(self.pin1,GPIO.HIGH)
					GPIO.output(self.pin2,GPIO.LOW)
					print("forward")
					x='z'
				else:
					GPIO.output(self.pin1,GPIO.LOW)
					GPIO.output(self.pin2,GPIO.HIGH)
					print("backward")
					x='z'


			elif x=='s':
				print("stop")
				GPIO.output(self.pin1,GPIO.LOW)
				GPIO.output(self.pin2,GPIO.LOW)
				x='z'

			elif x=='f':
				print("forward")
				GPIO.output(self.pin1,GPIO.HIGH)
				GPIO.output(self.pin2,GPIO.LOW)
				temp1=1
				x='z'

			elif x=='b':
				print("backward")
				GPIO.output(self.pin1,GPIO.LOW)
				GPIO.output(self.pin2,GPIO.HIGH)
				temp1=0
				x='z'

			elif x=='l':
				print("low")
				p.ChangeDutyCycle(25)
				x='z'

			elif x=='m':
				print("medium")
				p.ChangeDutyCycle(50)
				x='z'

			elif x=='h':
				print("high")
				p.ChangeDutyCycle(75)
				x='z'
			
			
			elif x=='e':
				GPIO.cleanup()
				break
			
			else:
				print("<<<  wrong data  >>>")
				print("please enter the defined data to continue.....")
			
class PAPA:
	def __init__(self):
		pass

	def test(self):
		# ServoMoteur
		# => https://raspberry-lab.fr/Composants/Controler-Servo-Moteur-Raspberry-Francais/

		GPIO.setmode(GPIO.BCM)
		GPIO.setup(17, GPIO.OUT)
		GPIO.setwarnings(False)

		ajoutAngle = 5

		print("\n+----------/ ServoMoteur  Controlleur /----------+")
		print("|                                                |")
		print("| Le Servo doit etre branche au pin 11 / GPIO 17 |")
		print("|                                                |")
		print("+------------------------------------------------+\n")

		print("Comment controler le Servo ?")
		choix = int(input("1. Choisir un angle\n2. Faire tourner de 0 a 180\n"))


		if (choix == 2) :
			nbrTour = int(input("Entrez le nombre d'aller-retour que fera le Servo :\n"))

			pwm=GPIO.PWM(17,100)
			pwm.start(5)

			angle1 = 0
			duty1 = float(angle1)/10 + ajoutAngle

			angle2=180
			duty2= float(angle2)/10 + ajoutAngle

			i = 0

			while i <= nbrTour:
				pwm.ChangeDutyCycle(duty1)
				time.sleep(0.8)
				pwm.ChangeDutyCycle(duty2)
				time.sleep(0.8)
				i = i+1
			GPIO.cleanup()

		if (choix == 1) :
			angle = float(input("Entrez l'angle souhaite :\n"))
			duree = int(input("Entrez la duree durant laquelle le Servo devra tenir sa position : ( en secondes )\n"))

			pwm=GPIO.PWM(17,100)
			pwm.start(5)

			angleChoisi = angle/10 + ajoutAngle
			pwm.ChangeDutyCycle(angleChoisi)
			time.sleep(duree)
			GPIO.cleanup()