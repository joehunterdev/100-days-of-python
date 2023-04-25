from cfg import *
from turtle import Turtle


class Ball(Turtle):

    def __init__(self):

        super().__init__("circle")

        # self.setx(0)
        # self.sety(0)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.left_score = 0
        self.right_score = 0

        self.y_move = 10

        self.color("white")
        # self.move_go()
        self.speed(1)

    def move_fd(self,left_bat,right_bat):


        if self.distance(self.xcor(),MAX_Y) < BALL_SIZE:
            print(f"Roof")
            self.rebound_y()

        # if self.distance(right_bat) < BAT_WIDTH:
        #     self.reboundx()
        #     print(f"Right Bat")

        #Loop Through positions
        for n in range(-30,50,10):
           print(f"{(right_bat.xcor(),right_bat.ycor() + n)}")

           if self.distance(right_bat.xcor(),right_bat.ycor() + n) < BAT_WIDTH:
              print(f"Right Bat")
            #   self.right_score += 1
              self.rebound_x()
        print(f"\n")


        if self.distance(MAX_X,self.ycor()) < 2:
            print(f"Right net")
            self.setposition(0,0)
 
        print(f"Pos {self.position()}")
        print(f"L Bat Pos {left_bat.position()}")

        #Loop Through positions
        for n in range(-30,50,10):

           print(f"{(left_bat.xcor(),left_bat.ycor() + n)}")

           if self.distance(left_bat.xcor(),left_bat.ycor() + n) < BAT_WIDTH:
              print(f"Left Bat")
            #   self.left_score += 1
              self.rebound_x()
              
        print(f"\n")

        if self.distance(self.xcor(),MIN_Y) < BALL_SIZE:
            print(f"Bottom")
            self.rebound_y()



        if self.distance(MIN_X,self.ycor()) < 2:
            print(f"Left net")
            self.setposition(0,0)

            # self.reboundx()
            # # self.reset()

        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)


    def rebound_x(self):
        self.x_move*=-1

    def rebound_y(self):
        self.y_move*=-1



    # def move_go(self):

    #     #go to top  right
    #     self.goto(MAX_X,MAX_Y)
    #     print(f"Current Heading {self.heading} ")
    #     self.right(45)
    #     self.forward(WIDTH)
    #     print(f"Current Heading {self.heading} ")


    #      # if distance to top right > 10


