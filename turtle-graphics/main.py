import turtle
import random

# draw a square

# t = turtle.Turtle()
# a square
# turtle.forward(100)
# turtle.right(90)
#
# turtle.forward(100)
# turtle.right(90)
#
# turtle.forward(100)
# turtle.right(90)
#
# turtle.forward(100)
# turtle.right(90)

t = turtle.Turtle()


def square():
    for i in range(3):
        turtle.forward(100)
        turtle.right(90)


def abstract(numsides):
    deg = 360 / numsides
    for i in range(numsides):
        turtle.forward(100)
        turtle.right(deg)


def dash(legnth):
    for i in range(legnth):
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()


def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    turtle.color(R, G, B)


def random_walk():
    while 5 > 0:

        heading = 360 / 4 * int(random.randint(1,4))
        turtle.setheading(heading)
        turtle.forward(10)
        turtle.width(3)
        random_color()


def random_color():

    r_tuple = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    turtle.colormode(255)
    turtle.color(r_tuple)
    # print(rgb)

def spirograph():

    while 1 > 0:
        turtle.circle(100)
        turtle.right(random.randint(1,7))
        random_color()
        turtle.speed(99)




# square()
# dash(100)

# shapes various
# for i in range(4,1000):
#     abstract(i)
#     change_color()

# random_walk()
spirograph()
# we know a circle is 360 deg / ths by num sides will give u deg of angle


# Make circle
# repeat rotation

turtle.exitonclick()
