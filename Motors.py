class Motor:
	def __init__(self):
		print(type(self).__name__)
		
class DC(Motor):
	def __init__(self):
		super().__init__()
		
class PAPA(Motor):
	def __init__(self):
		super().__init__()