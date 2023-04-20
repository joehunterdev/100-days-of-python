from turtle import Turtle, Screen
from functools import partial
from snake import Snake
from board import Board
from random import randint

# Config
sc = Screen()
sn = Snake()
bd = Board(sn.head,sn.body)
sc.setup(bd.width,bd.height)


control = False
n = 0

colors = ["green","orange","blue","red","purple","yellow","grey","pink","green","orange","blue","red","purple","yellow","grey","pink","green","orange","blue","red","purple","yellow","grey","pink"]

#init list of snake postions
turtles = [Turtle() for n in range(len(sn.body))]

while bd.in_game:

    sc.title(f"Snake Game score is: {bd.score}")

    # Add Food
    f = Turtle()
    f.hideturtle()
    f.penup()
    f.setposition(bd.food)
    print(f"  food coords {bd.food}")
    f.shape("square")
    f.shapesize(1)
    f.color(colors[randint(1,4)])
    id = f.stamp()


    i = 0
    # print a list of objects
    for turtle in turtles:

        turtles[i].speed(10)
        turtles[i].pendown()
        turtles[i].shapesize(1)
        turtle.shape("square")
        turtles[i].color(colors[i])

        sc.onkey(partial(sn.set_direction, "Up"), "Up")
        sc.onkey(partial(sn.set_direction, "Down"), "Down")
        sc.onkey(partial(sn.set_direction, "Left"), "Left")
        sc.onkey(partial(sn.set_direction, "Right"), "Right")
        sc.onkey(partial(bd.reset, sc), "space")

        head = sn.get_next(sn.direction)

        if bd.is_back(head):

          print(f"cant move back: continuing {sn.directions[-1]} as to last record in {sn.directions}")
          sn.move(sn.directions[-2])

        elif bd.is_food(head):
          bd.score = bd.score +1
          print(f"You eat some food")
          turtles.append(Turtle())
          bd.generate_food()
          f = Turtle()
          f.hideturtle()
        #   f.clearstamp(id)
        #   f.clear()
        #   bd.food = (70 * randint(1,3), -70 * randint(1,3) )
          sn.grow(head)
          sn.move(sn.direction)

        elif bd.is_wall(head):
           print(f"You hit the wall")
           bd.in_game = False

        elif bd.is_body(head):
           print(f"You cant eat yourself")
           bd.in_game = False
        else:
            sn.move(sn.direction)

       # ultimatley we place here
        turtles[i].setpos(sn.body[i])
        print(f" head coord \n {bd.head}")
        turtles[i].stamp()
        sc.listen()

        i += 1
        print(f"  body coords {sn.body}")
        # turtles[i].penup()
        turtle.clear()

    # while




n +=1
sc.exitonclick()