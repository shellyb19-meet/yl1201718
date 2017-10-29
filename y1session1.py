import turtle
turtle.speed(100)
turtle.pensize(1)

angle = 20
for i in range(100):
	turtle.left(angle)
	for i in range(7):
		turtle.forward(120)
		turtle.left(90)

turtle.mainloop()