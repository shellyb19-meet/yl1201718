class Person(object):
	"""docstring for ClassName"""
	def __init__(self, name, age, gender,city):
		self.name = name
		self.age =age
		self.gender = gender
		self.city = city
	def breakfest(self, some_food):
		print("Yay!" + self.name + " is eating her "+ some_food+ " favorite breakfest!")
	def play(self, play):
		print("Yay!" + self.name + " is playing " + play + " his favorite game!")	
j = Person("Jef",16, "male", "Jerusalem")
j.breakfest("corn")
j.play("chesh")
