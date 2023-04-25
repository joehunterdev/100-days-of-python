from cfg import *
from bat import Bat
from board import Board

from turtle import Turtle, Screen
from ball import Ball

# turtle = Turtle()
screen = Screen()
screen.setup(WIDTH,HEIGHT,startx=-2200, starty=-200)
screen.bgcolor(BG_COLOR)
screen.title("Hi welcome to pong")

left_bat   = Bat(-320,0)
left_bat.controls("w","s")

right_bat  = Bat(320,0)
right_bat.controls("Up","Down")

ball = Ball()  




# screen.listen()
# screen.onkeypress(left_bat.up,"w")
# screen.onkeypress(left_bat.down,"s")
# screen.onkeypress(right_bat.up,"Up")
# screen.onkeypress(right_bat.down,"Down") 

# left_score  = Board(-50,250,30)  
# right_score = Board(50,250,30) 

while IN_GAME:
      
      # ball.forward(5)
      ball.move()  
   
      if ball.distance(ball.xcor(),MAX_Y) < BALL_SIZE:
         print(f"Roof")
         ball.rebound_y()

      # if ball.distance(right_bat) < BAT_WIDTH:
      #     ball.reboundx()
      #     print(f"Right Bat")

      #Loop Through positions
      for n in range(-30,50,10):
         print(f"{(right_bat.xcor(),right_bat.ycor() + n)}")

         if ball.distance(right_bat.xcor(),right_bat.ycor() + n) < BAT_WIDTH:
            print(f"Right Bat")
         #   ball.right_score += 1
            ball.rebound_x()
      print(f"\n")


      if ball.distance(MAX_X,ball.ycor()) < 2:
         print(f"Right net")
         ball.setposition(0,0)

      print(f"Pos {ball.position()}")
      print(f"L Bat Pos {left_bat.position()}")

      #Loop Through positions
      for n in range(-30,50,10):

         print(f"{(left_bat.xcor(),left_bat.ycor() + n)}")

         if ball.distance(left_bat.xcor(),left_bat.ycor() + n) < BAT_WIDTH:
            print(f"Left Bat")
            # ball.left_score += 1
            ball.rebound_x()
            
      print(f"\n")

      if ball.distance(ball.xcor(),MIN_Y) < BALL_SIZE:
         print(f"Bottom")
         ball.rebound_y()

      if ball.distance(MIN_X,ball.ycor()) < 2:
         print(f"Left net")
         ball.reboundx()
         
screen.update() 
   
screen.exitonclick()



