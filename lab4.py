class Animal(object):
	"""docstring for ClassName"""
	def __init__(self, sound,name,age,favorite_color):
		self.sound = sound
		self.name = name
		self.age = age
		self.favorite_color = favorite_color
	def eat(self,food):
		print("Yummy!" + self.name + " is eating " + food)
	def description(self):
		print(self.name + "is" + self.age + "years old and he loves the color" + self.favorite_color)
	def make_sound(self,time):
		print(self.sound*time)
a = Animal("lala", "Kuki", 18, "Blue")
a.eat("corn")
a.make_sound(5)
