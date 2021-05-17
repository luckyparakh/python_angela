from turtle import Turtle, Screen, colormode
from random import choice, randint

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue")


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


# Draw Square
for _ in range(4):
    timmy.forward(50)
    timmy.right(90)

# Dash Line
timmy.clear()
timmy.reset()
for i in range(10):
    if i % 2 == 0:
        timmy.color("blue")
    else:
        timmy.color("white")
    timmy.forward(10)

timmy.color("red")
for i in range(10):
    if i % 2 == 0:
        timmy.penup()
    else:
        timmy.pendown()
    timmy.forward(10)

# Draw Triangle, Square, till 10 sided polygon
# timmy.clear()
# timmy.reset()
# for side in range(3, 11):
#     angle = 360 / side
#     timmy.color(choice(colors))
#     while side > 0:
#         timmy.forward(100)
#         timmy.right(angle)
#         side -= 1

# Draw Random Walk
# timmy.clear()
# timmy.reset()
# angles = [0, 90, 180, 270]
# timmy.pensize(10)
# timmy.speed(0)
# for _ in range(50):
#     timmy.color(choice(colors))
#     timmy.forward(20)
#     timmy.right(choice(angles))

# Draw Random Walk with Random Color
# timmy.clear()
# timmy.reset()
# angles = [0, 90, 180, 270]
# timmy.pensize(5)
# timmy.speed(0)
# colormode(255)  # Need to set RGB to choose value from 0 to 255
# for _ in range(50):
#     timmy.color(random_color())
#     timmy.forward(20)
#     timmy.right(choice(angles))

# Draw Spirograph
timmy.clear()
timmy.reset()
timmy.speed('fastest')
colormode(255)  # Need to set RGB to choose value from 0 to 255
for angle in range(100):
    timmy.pencolor(random_color())
    timmy.right(angle)
    timmy.circle(50)

screen = Screen()
screen.exitonclick()
