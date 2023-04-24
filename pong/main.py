from cfg import *
from bat import Bat
from turtle import Turtle, Screen

# turtle = Turtle()
screen = Screen()
screen.setup(WIDTH,HEIGHT)
screen.bgcolor(BG_COLOR)
screen.title("Hi welcome to pong")


left_bat   = Bat(-340,0)
left_bat.controls("w","s")
right_bat  = Bat(340,0)
right_bat.controls("Up","Down")


# while IN_GAME:

#     # comment:
#     # end while

# screen.listen()
# screen.onkey(left_bat.up,"w")
# screen.onkey(left_bat.down,"s")
# screen.onkey(right_bat.up,"Up")
# screen.onkey(right_bat.down,"Down") 

screen.exitonclick()

