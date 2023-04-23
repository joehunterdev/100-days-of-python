from turtle import Screen
import time
from cfg import *
from snake import Snake

# Todo:  Move to board
screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.title(f"Snake Game score is: 0")
screen.bgcolor(BG_COLOR)
pieces = []


snake = Snake()

while IN_GAME:

    # update after segments have moved
    time.sleep(0.4)
    screen.update()
    
    snake.move()


screen.exitonclick()
     