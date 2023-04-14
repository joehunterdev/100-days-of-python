import colorgram as cg
import turtle
import random

color_list = cg.extract("hirst.jpg", 2 ** 32)
color_palette = []

for count in range(len(color_list)):
    rgb = color_list[count]
    color = rgb.rgb
    color_palette.append(color)

print(color_palette)

t = turtle.Turtle()

turtle.colormode(255)

rows = 10
cols = 8
i = 0
circle_size = 11
t.pensize(circle_size*2)
t.speed(200)
padding = circle_size * 4

# t.goto(circle_size/2 - screen.window_width()/2, screen.window_height()/2 - circle_size/2)

x = -abs(rows * 3 * circle_size)
y = cols * 3 * circle_size

for j in range(cols):

  t.penup()
  t.setposition(x,(j * padding) - y)

  for i in range(rows):
        i+1
        t.forward(padding)
        t.color(color_palette[random.randint(1,len(color_palette) - 1)])
        t.pendown()
        t.circle(circle_size)
        t.penup()

turtle.exitonclick()


import turtle
import math

# Set up the turtle screen
screen = turtle.Screen()
screen.setup(800, 600)
screen.title("Rotating Aerofoil")

# Create a turtle to draw the aerofoil
aerofoil = turtle.Turtle()
aerofoil.speed(0)
aerofoil.penup()

# Define the coordinates of the aerofoil
aerofoil_coords = [(0, 50), (20, 70), (100, 70), (120, 50), (100, 30), (20, 30)]

# Draw the aerofoil
aerofoil.goto(aerofoil_coords[0])
aerofoil.pendown()
for x, y in aerofoil_coords[1:]:
    aerofoil.goto(x, y)
aerofoil.goto(aerofoil_coords[0])

# Define the angle of rotation
angle = 0

# Define the function to rotate the aerofoil
def rotate_aerofoil():
    global angle
    aerofoil.clear()
    new_coords = []
    for x, y in aerofoil_coords:
        # Convert the coordinates to polar coordinates
        r = math.sqrt(x**2 + y**2)
        theta = math.atan2(y, x)
        # Rotate the angle by 1 degree
        new_theta = theta + math.radians(angle)
        # Convert back to Cartesian coordinates
        new_x = r * math.cos(new_theta)
        new_y = r * math.sin(new_theta)
        new_coords.append((new_x, new_y))
    # Draw the rotated aerofoil
    aerofoil.penup()
    aerofoil.goto(new_coords[0])
    aerofoil.pendown()
    for x, y in new_coords[1:]:
        aerofoil.goto(x, y)
    aerofoil.goto(new_coords[0])
    # Increase the angle of rotation
    angle += 1
    # Call the function again after 10 milliseconds
    screen.ontimer(rotate_aerofoil, 10)

# Start the rotation
rotate_aerofoil()

# Start the turtle main loop
turtle.mainloop()