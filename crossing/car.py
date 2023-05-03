from cfg import *
from turtle import Turtle
from random import randint
import time
class Car(Turtle):

    def __init__(self,y=None):

        super().__init__("square")
        
        self.hideturtle()
        self.penup()
        self.speed(2)
        self.setheading(180)
        self.shapesize(2,4,1)
        #self.screen.delay(randint(0,50))

        self.color(COLORS[randint(0,len(COLORS)  - 1)])
        ypos = y if y != None else self.lanes[randint(0,len(self.lanes) -1)]
        self.setposition(MAX_X +randint(0,MAX_X * 2),ypos)

        self.showturtle()
        self.x_move = -10
        self.y_move = -10
    
    def reset(self):
        self.setx(MAX_X)
    
    # def move_forw(self):
    #     time.sleep(randint(0,2))
    #     self.forward(400)  
    
    def speedup(self):
        self.speed(self.speed()+1)
    
    # def lanes(self):
    #     pass
    
    # def position_op(self):
    #     pass
    
    
        

    # def rebound_x(self):
    #     self.x_move*=-1

    # def rebound_y(self):
    #     self.y_move*=-1
