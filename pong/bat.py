from cfg import *
from turtle import Turtle, Screen


class Bat(Turtle):

    def __init__(self,x,y,heading = 90):

        super().__init__("square")
        
        # defaults
        # self.set_side(side)
        self.up_key = ""
        self.down_key= ""
        
        self.setx(x)
        self.sety(y)
        self.penup()
        self.color("white")
        self.setheading(heading)
        self.turtlesize(BAT_WIDTH, BAT_HEIGHT)
        # self.capture(up_key,down_key)
        
    """
         Set Side Specifics   
    """
    def set_side(self, side):

        match (side):

            case ("Left"):
                self.setx(int(-abs(WIDTH / 2)))
                # self.up_key = "w"
                # self.down_key = "s"

            case ("Right"):
                self.setx((WIDTH / 2))
                # self.up_key = "Up"
                # self.down_key = "Down"

    """
        Move Bat Up
    """
    def up(self):
        print("uppin")
        if self.distance(self.xcor(), MAX_Y) > BAT_HEIGHT:
            self.forward(10)
        else:
            print(f"Bat hit ceiling, distance to ceil {self.distance(350,MAX_Y)}")
   
    """
        Move Bat Down
    """
    def down(self):
        if self.distance(self.xcor(), MIN_Y) > BAT_HEIGHT:
            self.backward(10)
            
    """
        Move Bat Up Other
    """
    def upb(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)
        # print("uppin")
        # if self.distance(self.xcor(), MAX_Y) > BAT_HEIGHT:
        #     self.forward(10)
        # else:
        #     print(f"Bat hit ceiling, distance to ceil {self.distance(350,MAX_Y)}")
   
    """
        Move Bat Down Other
    """
    def downb(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)


    """
        Capture Key Movement
    """
    def capture(self):

        self.screen.listen()
        self.screen.onkeypress(self.upb,self.up_key)
        self.screen.onkeypress(self.downb,self.down_key)
        
        
    def controls(self,up_key,down_key):   
        self.up_key = up_key
        self.down_key = down_key
        self.capture()
