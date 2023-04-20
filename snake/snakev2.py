from turtle import Turtle, Screen
from functools import partial
from snake import Snake
from food import Food
from board import Board
from random import randint
import time

# Config
sc = Screen()
sn = Snake()
fo = Food()
bd = Board()

sc.setup(bd.width,bd.height)
sc.bgcolor("black")
sc.title(f"Snake Game score is: {bd.score}")
sc.tracer(0)

#Initial list of snake postions
positions = [Turtle() for n in range(len(sn.pieces))]

while bd.in_game:

    sc.update()
    time.sleep(0.1)
    i = 0

    # print a list of objects
    for position in positions:
        
        new_piece = Turtle("square")
        new_piece.color("white")
        new_piece.penup()
        sn.move("Right")
        new_piece.goto(sn.pieces[i])
        i += 1
        print(f"{sn.pieces}")

sc.exitonclick()