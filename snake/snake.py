from turtle import Turtle, Screen
from cfg import *
from functools import partial
 

class Snake:
    
    def __init__(self):

      self.body = [(0, 0),(20, 0),(40, 0),(60, 0),(80, 0),(100, 0)]
      self.legnth = len(self.body)
    #    the next square
      self.head = ()
      self.speed = 1
      self.direction = "Right"
      self.directions = ["Right"]
      self.size = 20

    def move(self,key):
 
        match key:

            case "Up":

                head = (self.body[-1][0],self.body[-1][1]+self.size)

            case "Down":

                head = (self.body[-1][0],self.body[-1][1]-self.size)

            case "Left":

                head = (self.body[-1][0]-self.size,self.body[-1][1])

            case "Right":

                head = (self.body[-1][0] + self.size,self.body[-1][1])       
        
        self.pieces = []
        self.create()
        self.head = self.pieces[0]
        # self.capture()

    def create(self):   

        for postion in INIT_POSITIONS:
            # new object
            new_piece = Turtle("square")
            new_piece.penup()
            new_piece.color("white")
            new_piece.goto(postion)           

            # add new piece obj with coords
            self.pieces.append(new_piece)
            
    def extend(self):
        self.grow(self.pieces[-1].position())
        
    def move(self):
            self.capture()
            # print(f"Pieces {self.pieces}")
            #Get 2nd to last piece and go backwards
            for piece in range(len(self.pieces) - 1, 0, -1):
                    
                    #Reposition piece based on the previous
                    self.pieces[piece].goto(self.pieces[piece - 1].xcor(),self.pieces[piece - 1].ycor())
            
            #Apply Movement         
            self.head.forward(PIECE_SIZE)
            self.head.speed(10)

    
    def heading(self,deg):
    
        # print(f"Cur head {self.head.heading()} + Proposed {deg}  ")
        # print(f"Oposite Angle: {(int(deg) + 180) % 360} ")
        self.head.hideturtle()
        if self.head.heading() != (int(deg) + 180) % 360: 
            # self.head.penup()
            self.head.setheading(deg)

        # else: 
            
        #     print(f"Cant reverse direction")

    def capture(self):
        
        screen = Screen()

        screen.onkey(partial(self.heading, 90),"Up")
        screen.onkey(partial(self.heading, 270),"Down")
        screen.onkey(partial(self.heading, 180),"Left")
        screen.onkey(partial(self.heading, 0),"Right")

        screen.listen()
    
    def grow(self,pos):
    
        add_piece = Turtle("square")
        add_piece.color("white")
        add_piece.penup()
        add_piece.setpos(pos)
        self.pieces.append(add_piece)

    def next_pos(self):
        
       # partial(self.heading, 90)
        next_piece = Turtle("square")
        next_piece.hideturtle()
        next_piece.color("grey")
        next_piece.penup()
        next_piece.setheading(self.head.heading())
        next_piece.goto(self.head.position())
        next_piece.forward(PIECE_SIZE)
        

        return next_piece.position()