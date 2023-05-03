from cfg import *
from turtle import Turtle, Screen


class Player(Turtle):

    def __init__(self,y,heading = 90):

        super().__init__()

        self.color("black")
        self.pensize(PLAYER_SIZE)
        self.shapesize(2,2,1)
        self.setheading(heading)
        # self.turtlesize(PLAYER_SIZE, PLAYER_SIZE)
        self.penup()
        self.setx(0)
        self.sety(-200)
        self.capture()

    def up(self):

        if self.distance(self.xcor(), MAX_Y) > PLAYER_SIZE:
            self.forward(PLAYER_SIZE)
        else:
            print(f"You Crossed {self.distance(350,MAX_Y)}")
   
    def down(self):
        if self.distance(self.xcor(), MIN_Y) > PLAYER_SIZE:
            self.backward(PLAYER_SIZE)

    def capture(self):

        self.screen.listen()
        self.screen.onkeypress(self.up,"Up")
        self.screen.onkeypress(self.down,"Down")
        
 