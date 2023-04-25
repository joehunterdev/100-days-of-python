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

ball = Ball()  




# screen.listen()
# screen.onkeypress(left_bat.up,"w")
# screen.onkeypress(left_bat.down,"s")
# screen.onkeypress(right_bat.up,"Up")
# screen.onkeypress(right_bat.down,"Down") 

# left_score  = Board(-50,250,30)  
# right_score = Board(50,250,30) 

while IN_GAME:
       
   # ball.forward(5)
   ball.move_fd(left_bat,right_bat)  
   # left_score.text(ball.left_score)
   # right_score.text(ball.right_score)
   screen.update() 
   
screen.exitonclick()



