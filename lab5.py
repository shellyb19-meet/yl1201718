import turtle
from turtle import*
colormode(255)
import random
red=random.randint(0,225)
green=random.randint(0,225)
blue=random.randint(0,225)


class Rectangle(Turtle):
	def __init__(self,width,height):
		Turtle. __init__(self)
		self.width=width
		self.height=height
		turtle.register_shape("rectangle",((height,0),(height,width),(0,width),(0,0)))
		turtle.shape("rectangle")
		self.setheading(90)
class Square(Rectangle):
	def __init__(self, size):
		Rectangle. __init__(self,size,size)
		 
	def random_color(self):
		self.shape("square")
		self.color(red,green,blue)
		print(red,green,blue)

class Hexagon(Turtle):
	def __init__(self, size):
		Turtle. __init__(self)
		turtle.home()
		turtle.speed(100)
		turtle.begin_poly()
		for i in range(6):
			turtle.fd(60)
			turtle.right(60)
		turtle.end_poly()
		p = turtle.get_poly()
		turtle.register_shape("bill",p)
		turtle.shape("bill")


#rectangle123=rectangle(10,20)
bob = Hexagon(5)
print(bob)
#bob.random_color()
turtle.mainloop()
