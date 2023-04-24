from turtle import Screen
import time
from cfg import *
from snake import Snake
from board import Board
from food import Food
# Todo:  Move to board
screen = Screen()
screen.setup(width=WIDTH,height=HEIGHT)
screen.bgcolor(BG_COLOR)
snake = Snake()

food = Food()
board = Board()
# screen.tracer(1,1)
while IN_GAME:
    # time.sleep(0.1)
 
    # update after segments have moved
    snake.move()
    screen.title(f"Snake Game score is : {board.score}")
    board.add_board(f"Score {board.score}",BORDERS)

    # print(f"Head->{snake.head.position()}")
    
    if snake.head.position() == food.position():
        snake.extend()
        board.add_board(f"Eating some food",120)
        food.random_pos()        
        board.add_score(1)
    elif snake.head.xcor() >= (BORDERS) or snake.head.xcor() <= -abs(BORDERS):
        board.add_board("You hit the wall side",100)
        # board.is_wall()
        IN_GAME = False

    elif snake.head.ycor() >= BORDERS or snake.head.ycor() <= -abs(BORDERS) :
        board.add_board("You hit the top/bottom wall",100)
        # board.is_wall()
        IN_GAME = False

    positions = [snake.position() for snake in snake.pieces]   
 
    if snake.next_pos() in positions:
        board.add_board("You cant eat Yourself " +snake.next_pos(positions),100)
        IN_GAME = False
  
    screen.update()

else:
   board.add_board(f"Game Over",200)
   time.sleep(4)
   IN_GAME = True
   screen.reset()
screen.exitonclick()
