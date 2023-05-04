from cfg import *
from turtle import Turtle,Screen

class Board(Turtle):

    def __init__(self,x,score):
        super().__init__()
        
        self.hideturtle()
        self.penup()
        self.color('white')
        self.style = ('Arial', 30, 'italic')
        self.score = score
        self.xpos = x
        self.place_top(x)
   
    def place_top(self,xpos):
        self.clear()
        self.setposition(xpos,210)
        self.write(self.score, font=self.style, align='left')
 
    def update_score(self,score):
        self.score =  self.score + score
        self.place_top(self.xpos)