from turtle import Screen
import time
from cfg import *
from snake import Snake
from board import Board
from food import Food

screen = Screen()
screen.setup(width=WIDTH,height=HEIGHT)
screen.bgcolor(BG_COLOR)

snake = Snake()
food  = Food()
board = Board()

screen.tracer(0,1)

while IN_GAME:
    
    time.sleep(0.1)
     # update after segments have moved
    snake.move()
    screen.title(f"Snake Game score is : {board.score}")
    board.add_board(f"Score {board.score}",-abs(BORDERS) + 10)
    board.add_board(f"High Score {board.high_score}",BORDERS + 10)
   
    # if snake.head.position() == food.position():
    #     snake.extend()
    #     board.add_board(f"Eating some food",120)
    #     food.random_pos()        
    #     board.add_score(1)
      
    if snake.head.distance(food) < 10:
        snake.extend()
        board.add_board(f"Eating some food",120)
        food.random_pos()        
        board.add_score(1)
             
    if snake.head.xcor() >= (BORDERS) or snake.head.xcor() <= -abs(BORDERS):
        board.add_board("You hit the wall side",100)
        # board.is_wall()
        IN_GAME = False

    elif snake.head.ycor() >= BORDERS or snake.head.ycor() <= -abs(BORDERS) :
        board.add_board("You hit the top/bottom wall",100)
        # board.is_wall()
        IN_GAME = False

    positions = [snake.position() for snake in snake.pieces]   
 
    if snake.next_pos() in positions:
        board.add_board("You cant eat Yourself ",-300,10)
        IN_GAME = False
    
    screen.update()
    
else:
    
    board.add_board("Game Over",200)
    time.sleep(2)
    board.restart()
    board.add_board(f"High Score {board.high_score}",BORDERS)
    # screen.update()
    # snake.pieces.clear
    # food.clear()
    # snake.restart()
    # screen.update()
    # IN_GAME = True
    # print(f"Reseting: {IN_GAME}")
    # continue

screen.exitonclick()
