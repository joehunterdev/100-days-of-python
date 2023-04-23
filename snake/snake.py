from turtle import Turtle, Screen
from cfg import *

class Snake:
    
    def __init__(self):
        
        self.pieces = []
        self.create()
        self.head = self.pieces[-1]

    def create(self):            

        for postion in INIT_POSITIONS:
            
            # new object
            new_piece = Turtle("square")
            new_piece.color("white")
            new_piece.penup()
            new_piece.goto(postion)
            
            # add new piece obj with coords
            self.pieces.append(new_piece)
            
    
    def move(self):
            
            #Get 2nd to last piece and go backwards
            for piece in range(len(self.pieces) - 1, 0, -1):
                    
                    #Reposition piece based on the previous
                    self.pieces[piece].goto(self.pieces[piece - 1].xcor(),self.pieces[piece - 1].ycor())
            
            #Apply Movement         
            self.pieces[0].forward(PIECE_SIZE)

    