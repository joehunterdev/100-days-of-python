from turtle import Turtle,Screen
from cfg import *
class Board(Turtle):

    def __init__(self):

      super().__init__()
      self.score = 0
      self.penup()
      self.high_score =  0
      self.player_name = "Joey"
      self.read_high_score() 
      
       
    def add_board(self,text,position,fsize =20):
      self.setpos(0,-position)
      style = ('System', fsize, 'italic')
      self.color("white")
      self.hideturtle()
      self.write(text, font=style, align='center')

    def add_score(self,points = 1):
      self.score += points
      self.clear()
    
    def restart(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score()
        self.score = 0
        self.add_score()

    def read_high_score(self):
      
      with open(DIR_PATH+"score.txt", mode ="r") as hs:
        self.high_score = int(hs.read())      
        # print(f"hs {type(hs)}")
    
    def write_high_score(self):
      with open(DIR_PATH+"score.txt", mode ="w") as file:
          file.write(str(self.high_score))