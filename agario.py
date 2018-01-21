import turtle
import time
import random
import Ball
turtle.tracer(0)
turtle.hideturtle()
RUNNING=True
SLEEP=0.0077
SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2

MY_BALL=Ball()
NUMBER_OF_BALLS=5
MINIMUM_BALL_RADIUS=10
MAXIMUM_BALL_RADIUS=100
MINIMUM_BALL_DX=-5
MAXIMUM_BALL_DX=5
MINIMUM_BALL_DY=-5
MAXIMUM_BALL_DY=5
BALLS=[]
for i in range(NUMBER_OF_BALLS):
	x=random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS, SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
	y=random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
	dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
	dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
	r=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
	color=(random.random(),random.random(),random.random())
	new_ball=Ball(x,y,dx,dy,r,color)
	BALLS.append(new_ball)
def move_all_balls():
	for ball in BALLS:
		ball.move(SCREEN_WIDTH,SCREEN_HEIGHT)
def collide(ball_a,ball_b):
	if(ball_a==ball_b):
		return(False)
	des=math.sqrt((y2-y)*(y2-y)+(x1-x)*(x1-x))
	if(des+10<=ball_a.r+ball_b.r):
		return(True)
	else:
		return(False)
def chek_all_balls_collision():
	for ball_a in BALLS:
		for ball_b in BALLS:
			r_a=ball_a.r
			r_b=ball_b.r
			new_x=random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS, SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
			new_y=random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
			new_dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
			new_dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
			new_r=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
			new_color=(random.random(),random.random(),random.random())
			if(r_a>r_b):
				r_a=r_a+1
				ball_b.x=new_x
				ball_b.y=new_y
				ball_b.dx=new_dx
				ball_b.dy=new_dy
				ball_b.r=new_r
				ball_b.color=new_color
			else:
				r_b=r_b+1
				ball_a.x=new_x
				ball_a.y=new_y
				ball_a.dx=new_dx
				ball_a.dy=new_dy
				ball_a.r=new_r
				ball_a.color=new_color
def check_myball_collision():
	for balli in BALLS:
		if(MY_BALL==balli):
			r_m=MY_BALL.r
			r_ba=balli.r
			if(r_ba>r_m):
				return(False)
			else:
				r_m=r_m+1
				balli.x=new_x
				balli.y=new_y
				balli.dx=new_dx
				balli.dy=new_dy
				balli.r=new_r
				balli.color=new_color
	return(True)
def movearound(event):
	MY_BALL.goto(event.x-SCREEN_WIDTH,SCREEN_HEIGHT-event.y)
turtle.getcanvas().bind("<Motion>",movearound)
turtle.getscreen().listen()
while(RUNNING==true):
	if(SCREEN_HEIGHT!=turtle.getcanvas().winfo_height()/2 and SCREEN_HEIGHT!=turtle.getcanvas().winfo_width()/2):
		SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2
		SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2
	else:
		move_all_balls()
		move(MY_BALL)
		







