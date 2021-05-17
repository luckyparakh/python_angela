import colorgram
from turtle import Turtle, Screen, colormode
from random import choice

# Extract colors from a image
colors = colorgram.extract('download.jpg', 10)
colors_rgb = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    colors_rgb.append((r, g, b))

# Set color mode to use RGB value.
colormode(255)

# screen.screensize(700,700)
# screen.bgcolor("black")


screen = Screen()
screen.bgcolor("black")
tim = Turtle()
tim.speed('fastest')
for y in range(-300, 300, 60):
    for x in range(-300, 300, 60):
        tim.penup()
        tim.setpos(x, y)
        tim.dot(20, choice(colors_rgb))

screen.exitonclick()
