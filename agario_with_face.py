import turtle
import time
import random
from ball import Ball
import math
import numpy as np
import cv2

o=55
oo=125
heart=turtle.clone()
heart.up()
turtle.addshape("heart.gif")
heart.shape("heart.gif")
heart1=heart.clone()
heart2=heart.clone()
heart.goto(0,o)
heart1.goto(oo,o)
heart2.goto(oo-oo*2,o)
hear=3

turtle.bgcolor(random.randint(0,225),random.randint(0,225),random.randint(0,225))
turtle.tracer(0)
turtle.shape("blank")
RUNNING=True
SLEEP=0.0077
score = 1
SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2
red=random.randint(0,255)
green=random.randint(0,255)
blue=random.randint(0,255)


MY_BALL=Ball(5,7,0,0,30, (red,green,blue))
NUMBER_OF_BALLS=5
MINIMUM_BALL_RADIUS=10
MAXIMUM_BALL_RADIUS=70
MINIMUM_BALL_DX=-3
MAXIMUM_BALL_DX=3
MINIMUM_BALL_DY=-3
MAXIMUM_BALL_DY=3
BALLS=[]


for i in range(NUMBER_OF_BALLS):
	x=random.randint(int(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS), int(SCREEN_WIDTH-MAXIMUM_BALL_RADIUS))
	y=random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
	dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
	while dx==0:
		dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
	dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
	while dy==0:
		dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
	r=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
	color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
	NEW_BALL=Ball(x,y,dx,dy,r,color)
	BALLS.append(NEW_BALL)



def move_all_balls():
	for ball in BALLS:
		ball.move(SCREEN_WIDTH,SCREEN_HEIGHT)
def collide(ball_a,ball_b):
	if(ball_a==ball_b):
		return False
	y=ball_a.ycor()
	x=ball_a.xcor()
	y2=ball_b.ycor()
	x1=ball_b.xcor()
	sqrt=(y2-y)*(y2-y)+(x1-x)*(x1-x)
	des=math.sqrt(sqrt)
	if(des+10<=ball_a.r+ball_b.r):
		return True
	else:
		return False
def chek_all_balls_collision():
	for ball_a in BALLS:
		for ball_b in BALLS:
			if(collide(ball_a,ball_b)):
				r_a=ball_a.r
				r_b=ball_b.r
				new_x=random.randint(int(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS), int(SCREEN_WIDTH-MAXIMUM_BALL_RADIUS))
				new_y=random.randint(int(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS), int(SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS))
				new_dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
				while new_dx==0:
					new_dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
				new_dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
				while new_dy==0:
					new_dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
				new_r=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
				new_color=(int(random.random()*255),int(random.random()*255),int(random.random()*255))
				if(r_a>r_b):
					ball_a.r+=1
					ball_a.shapesize(ball_a.r/10)
					ball_b.goto(new_x, new_y)
					ball_b.dx=new_dx
					ball_b.dy=new_dy
					ball_b.r=new_r
					ball_b.color(new_color)
					ball_b.shapesize(new_r/10)
				else:
					ball_b.r+=1
					ball_b.shapesize(ball_b.r/10)
					ball_a.goto(new_x, new_y)
					ball_a.dx=new_dx
					ball_a.dy=new_dy
					ball_a.r=new_r
					ball_a.color(new_color)
					ball_a.shapesize(new_r/10)


def check_myball_collision():
	global score,hear
	for balli in BALLS:
		if(collide(balli,MY_BALL)):
			r_m=MY_BALL.r
			r_ba=balli.r
			neww_x=random.randint(int(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS), int(SCREEN_WIDTH-MAXIMUM_BALL_RADIUS))
			neww_y=random.randint(int(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS), int(SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS))
			neww_dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
			neww_dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
			neww_r=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
			neww_color=(int(random.random()*255),int(random.random()*255),int(random.random()*255))
			if(r_ba>r_m):
				hear=hear-1
				if(hear==2):
					heart2.hideturtle()
					balli.goto(neww_x,neww_y)
					balli.dx=neww_dx
					balli.dy=neww_dy
					balli.r=neww_r
					balli.color(neww_color)
					balli.shapesize(neww_r/10)
				if(hear==1):
					heart.hideturtle()
					balli.goto(neww_x,neww_y)
					balli.dx=neww_dx
					balli.dy=neww_dy
					balli.r=neww_r
					balli.color(neww_color)
					balli.shapesize(neww_r/10)
				if(hear==0):
					heart1.hideturtle()
					return False
			else:
				MY_BALL.r += 1
				MY_BALL.shapesize(MY_BALL.r/10)
				balli.goto(neww_x,neww_y)
				balli.dx=neww_dx
				balli.dy=neww_dy
				balli.r=neww_r
				balli.color(neww_color)
				balli.shapesize(neww_r/10)
				turtle.clear()
				turtle.home()
				turtle.write("SCORE: " + str(score), True, align="center",font=("Arial", 25, "normal"))
				score=score+1
	return True
p=0
def movearound(event):
	MY_BALL.goto(event.x-SCREEN_WIDTH,SCREEN_HEIGHT-event.y)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
cap = cv2.VideoCapture(0)

#turtle.getcanvas().bind(face_move,movearound)
#turtle.getscreen().listen()
turtle.getcanvas().bind("<Motion>",movearound)
turtle.getscreen().listen()

while RUNNING==True:
	if(SCREEN_WIDTH!=turtle.getcanvas().winfo_width()/2) or SCREEN_HEIGHT!=turtle.getcanvas().winfo_height()/2:
		SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2
		SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2
	move_all_balls()
	chek_all_balls_collision()
	#MY_BALL.move(SCREEN_WIDTH,SCREEN_HEIGHT)
	RUNNING=check_myball_collision()
	
		
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, flags=0, minSize=(128,128))
	# for (x,y,w,h) in faces:
	# 	cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
	# 	roi_gray = gray[y:y+h, x:x+w]
	# 	roi_color = frame[y:y+h, x:x+w]
	# 	eyes = eye_cascade.detectMultiScale(roi_gray)
	# 	for (ex,ey,ew,eh) in eyes:
	# 		cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
	# cv2.imshow('frame',frame)
	# if cv2.waitKey(1) & 0xFF == ord('q'):
	# 	break
	
	print(faces)
	if len(faces)>0:
		xf=faces[0][0]*2-SCREEN_WIDTH
		yf=SCREEN_HEIGHT-faces[0][1]*2
		MY_BALL.goto(-xf,yf)
	p=p+1
	turtle.getscreen().update()
	time.sleep(SLEEP)

cap.release()
cv2.destroyAllWindows()
turtle.clear()
turtle.home()
turtle.write("GAME OVER", True, align="center",font=("Arial",35, "normal"))




turtle.mainloop()







