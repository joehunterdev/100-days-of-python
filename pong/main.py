from cfg import *
from bat import Bat
from turtle import Turtle, Screen

# turtle = Turtle()
sc = Screen()
sc.setup(WIDTH,HEIGHT)
sc.bgcolor(BG_COLOR)
sc.title("Hi welcome to pong")

left   = Bat(-340,0)
left.controls("w","s")
# left.capture()
right  = Bat(340,0)
# right.capture()w
right.controls("Up","Down")


# while IN_GAME:

#     # comment:
#     # end while

sc.exitonclick()

