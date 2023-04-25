from cfg import *
from turtle import Turtle


class Ball(Turtle):

    def __init__(self):

        super().__init__("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10

        self.color("white")
        self.speed(1)

    def move(self):

        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)
    
    def speedup(self):
        self.speed(self.speed()+1)

    def rebound_x(self):
        self.x_move*=-1

    def rebound_y(self):
        self.y_move*=-1

