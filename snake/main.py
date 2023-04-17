from turtle import Turtle, Screen
# from functools import partial
from random import randint
from functools import partial

# Classic Snake game Challenge

# TODO 1. Snake body:

    #[]Defie Start pos 0
    #[]Snake head should be one move ahead checknextmove(d1)
    #[x]Snake body can grow in legnth
    #[x]Snake can body move
    #[x] Numerical array ?/ pop push ? / tupples

# TODO 2. Move Snake:
#       [x]Snake moves forward automatically
#       [x]Snake must continue on same trajectory if not controlled
#       [x]Snake body coords must appear and disappaer from arr
#       [ ]Dont allow snake to reverse direction on itself
#
#
#
# TODO 3. Control Snake:
#
# TODO 4. Detect Colision with food
#     if snake head is in wanted co-ord
#       add to snake_body->legnth (adding to tail ?)

# TODO 5. Create Score board:
#   Total of foods eaten
#   [] Speed would increase difficulty

# TODO 6. Detect collision with wall:
#     while is_allowed(snake_head,coords) display score
#         else exit
# TODO 7. Detect collision with tail:
#     exit display score
#     while is_allowed(snake_head,coord) display score
#         else exit
# TODO 9. Bug:
#     [] init bug splitting lines to draw snake


class Snake:

    def __init__(self):

      self.body = [(0, 0), (30, 0), (60, 0),  (90, 0), (110, 0)]
      self.legnth = 3
      self.head = self.body[-1]
      self.speed = 1
      self.direction = "Up"

    def move(self,key):

        if key == "Up" and self.direction != "Down":
            self.body.append((self.body[-1][0],self.body[-1][1]+10))
        # else:
        #     self.body.append((self.body[-1][0],self.body[-1][1]-10))
        #     return
        if key == "Down" and self.direction != "Up":
            self.body.append((self.body[-1][0],self.body[-1][1]-10))
        if key == "Left" and self.direction != "Right":
            self.body.append((self.body[-1][0] - 10,self.body[-1][1]))
        if key == "Right" and self.direction != "Left":
            self.body.append((self.body[-1][0] + 10,self.body[-1][1]))
        # else:
        #     self.body.append((self.body[-1][0] + 10, self.body[-1][1]))
        self.body.pop(0)

    def grow_snake(self):
        self.body.append(self.head)
        pass

    def set_direction(self,key):
        self.direction = key
    # def grow_snake(self):
    #     self.body.append(self.head)
    #     pass

    def draw_snake(self):
        pass

class Board:

    def __init__(self,head,body):

        self.width = 600
        self.height = 600
        self.coord = (0,0)
        self.walls = (self.width -1,self.height -1)
        self.food = randint(1,4)
        self.score = 0

    # def is_allowed(self):
    #
    #         # if self.is_wall() == None | self.is_body() == None:
    #         #
    #         # return True

    # def is_wall(self):
    #
    #         # if head !in_array()
    #         # pos_walls =  (self.width -1,self.height -1)
    #         # neg_walls =  (-abs(self.width) + 1, -abs(self.width) + 1)
    #
    #    return True

    def is_food(self):
       return True

    def is_body(self):
       pass


# Config
sc = Screen()
sn = Snake()

bd = Board(sn.head,sn.body)
sc.screensize(bd.width,bd.height)
# print(f"Score is :{bd.score}")
sc.title("Snake Game score is: ")
turtles = [Turtle() for n in range(sn.legnth)]

# add to list of tuples
# sn.body.append((11,22))

control = False
n = 0

colors = ["green","orange","blue","red","purple"]

# def move():
#
#
# def rotate(deg):
#
#      turtles[i].right(deg)
#      turtles[i].fd(10)
#      print(f"moving {10}")

def reset():
    sc.reset()

while n < 10:

    i = 0

    for turtle in turtles:

        turtles[i].pendown()
        turtles[i].shapesize(1)
        turtle.shape("square")
        turtles[i].color(colors[i])

        sc.onkey(partial(sn.set_direction, "Up"), "Up")
        sc.onkey(partial(sn.set_direction, "Down"), "Down")
        sc.onkey(partial(sn.set_direction, "Left"), "Left")
        sc.onkey(partial(sn.set_direction, "Right"), "Right")

        sn.move(sn.direction)

        turtles[i].setpos(sn.body[i])
        print(f" head coord \n {sn.body[i]}")
        # turtles[i].setpos(turtles[i].pos())
        turtles[i].stamp()
        sc.listen()

        i += 1
        print(f"  body coords {sn.body}")
        # turtles[i].penup()
        turtle.clear()

n +=1

sc.exitonclick()