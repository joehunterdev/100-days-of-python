from cfg import *
from bat import Bat
from board import Board

from turtle import Turtle, Screen
from ball import Ball

# turtle = Turtle()
screen = Screen()
screen.setup(WIDTH,HEIGHT,startx=-2200, starty=-200)
screen.bgcolor(BG_COLOR)
screen.title("Hi welcome to pong")

left_bat   = Bat(-320,0)
left_bat.controls("w","s")

right_bat  = Bat(320,0)
right_bat.controls("Up","Down")

ball   = Ball()
left_board  = Board(-80,0)
right_board = Board(80,0)

i = 1
while IN_GAME:

      screen.update()
      ball.move()

      if ball.distance(ball.xcor(),MAX_Y) < BALL_SIZE or  ball.distance(ball.xcor(),MIN_Y) < BALL_SIZE:
         print(f"Roof / Ceil")
         ball.rebound_y()

      #Loop Through positions
      for n in range(-30,50,10):

         if ball.distance(right_bat.xcor(),right_bat.ycor() + n) < BAT_WIDTH:
            print(f"Right Bat")
            ball.rebound_x()
            i +=1
            ball.speed(i)

         if ball.distance(left_bat.xcor(),left_bat.ycor() + n) < BAT_WIDTH:
            print(f"Left Bat")
            ball.rebound_x()
            i +=1
            ball.speed(i)

      if ball.distance(MAX_X,ball.ycor()) < 2:
            print(f"Right net")
            ball.rebound_x()
            left_board.update_score(1)

      if ball.distance(MIN_X,ball.ycor()) < 2:
            print(f"Left net")
            ball.rebound_x()
            right_board.update_score(1)
  

screen.exitonclick()



