from cfg import *
from turtle import Turtle


class Board(Turtle):

    def __init__(self,x,y,fsize,text):
        
        super().__init__()
        
        self.setx(x)
        self.sety(y)
        self.color("white")
        self.fsize = fsize
        self.hideturtle()
        self.penup()
        # self.size(ssize)
        # self.scores()
        # self.font = "Courier"
            
    def text(self,text):
        
       self.write(text,False,"left",self.fsize)    

    def right_score(self):
        
         self.setx(120)
         self.write(self.score)