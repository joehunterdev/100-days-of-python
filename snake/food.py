from turtle import Turtle, Screen
from cfg import *
from random import randint

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(2)
        # self.setpos(140,00)
        self.random_pos() # Required 
        # self.create()

    def random_pos(self):
        self.goto(randint(1,11)*20,randint(1,11)*20)
        
    def debug_pos(self):
        new_x = self.ycor() + 20
        self.goto(new_x,0)
