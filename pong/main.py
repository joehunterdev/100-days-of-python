from cfg import *
from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()
screen.setup(WIDTH,HEIGHT)
screen.bgcolor(BG_COLOR)

screen.title("Hi welcome to pong")

def bat_up():

    if bat.distance(350,MAX_Y) > BAT_HEIGHT:
      bat.forward(10)
    # else:
    #     print(f"Bat hit ceiling, distance to ceil {bat.distance(350,MAX_Y)}")

def bat_down():

   if bat.distance(350,MIN_Y) > BAT_HEIGHT:
      bat.backward(10)
#    else:
#         print(f"Bat hit floor, distance to floor {bat.distance(350,MAX_Y)}")


bat = Turtle()
bat.setpos(350,0)
bat.goto(350,0)
bat.penup()
bat.shape("square")
bat.color("white")
bat.setheading(90)
bat.turtlesize(2,10)

#Perform Bat stuff
screen.onkeypress(bat_up,"Up")
screen.onkeypress(bat_down,"Down")

screen.listen()

# while IN_GAME:

#     # comment:
#     # end while

screen.exitonclick()

