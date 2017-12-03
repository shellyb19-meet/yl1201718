from turtle import*
import random
import math

class Ball(Turtle):
	def __init__(self, radius, color, speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius)
		self.color(color)
		self.speed(speed)

bob=Ball(7,"blue",300)
boni=Ball(9,"green",87)

x = bob.xcor()
y=bob.ycor()

bob.goto(x,y)

x1=boni.xcor()
y2=boni.ycor()

boni.goto(40,40)

des=math.sqrt((y2-y)*(y2-y)+(x1-x)*(x1-x))
def check_collision(bob,boni):
	#if bob.r+boni.r > distance between the center of the two balls
	if(bob.radius+boni.radius>des):
		bob.color("pink")



check_collision(bob,boni)
mainloop()





