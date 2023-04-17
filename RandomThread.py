import threading

from random import randint
from time import sleep

class RandomThread(threading.Thread):
	def __init__(self, name):
		super(RandomThread, self).__init__()
		self.setName(name)
		
	def run(self):
		execution_time = randint(1, 5)
		print("Starting " + self.getName())
		sleep(execution_time)
		print("Exiting " + threading.current_thread().getName())