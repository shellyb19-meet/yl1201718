import turtle
turtle.register_shape("yay",((50,0), (50,-25), (25,-50), (0,-25), (0,0)))
turtle.shape("yay")
for i in range(5):
	turtle.forward(50)
	turtle.right(145)
turtle.mainloop()


