import turtle
turtle.addshape("Feather-Transparent.gif")
turtle.shape("Feather-Transparent.gif")
angle=1
turtle.speed(3000)
for i in range(360):
	turtle.forward(300)
	turtle.right(60)
	turtle.forward(100)
	turtle.right(90)
	turtle.forward(70)
	turtle.home()
	turtle.right(angle)
	angle=angle+1
	 
turtle.mainloop()