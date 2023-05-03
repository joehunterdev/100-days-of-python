from cfg import *
from turtle import Turtle,Screen
from player import Player
from car import Car
from random import shuffle,randint
import time

screen = Screen()
screen.setup(800,600,startx=-2400, starty=-200)
screen.bgcolor(BG_COLOR)

screen.title("Hi welcome to Crossing")
player = Player(-200)

level = 1
n = 0
screen.tracer(0,1)

traffic = []

# Generate 7 Lanes of traffic
for i in range(-100,300,60):
    traffic.append(Car(i))

while IN_GAME:

    match (level):

        ## Level 2
        case (2):
            lanes = (2,6,0,5)

        case (3):
            lanes = (2,6,1,3,5)

        case (4):
            # 7 Lanes
            lanes = (2,6,3,1,4,0,5)
        ## Level 1
        case _:
            lanes = (2,6,4)
            #lanes = (0,1)

    # Fire lanes
    for lane in lanes:
        # Check is out of bounds
        if traffic[lane].xcor() < MIN_X:
            traffic[lane].reset()
        traffic[lane].forward(randint(0,10))
        
        # Detect colision
        if player.distance(traffic[lane]) < 34:

            print(f"Current Distance to car {lane}: {player.distance(traffic[lane])}")
            print("Game Over")
            IN_GAME = False

        if player.distance(player.xcor(), MAX_Y) < PLAYER_SIZE:
            print(f"You made it to the next level: {level}")
            player.sety(-200)
            level +=1


    screen.update()
    time.sleep(0.1)

#screen.update()
screen.exitonclick()
