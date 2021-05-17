from turtle import Turtle, Screen
from random import randint
is_race_start = False
colours = ['red', 'yellow', 'orange', 'green', 'blue', 'purple']
screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput("Make your Bet", "Choose Color of Turtle that will win:")
turtles = []
winner = ""

if user_input in colours:
    is_race_start = True

cor_y = -50
for colour in colours:
    new_turtle = Turtle()
    new_turtle.shape('turtle')
    new_turtle.penup()
    new_turtle.color(colour)
    new_turtle.goto(-230, cor_y)
    cor_y += 40
    turtles.append(new_turtle)

while is_race_start:
    for racer in turtles:
        racer.forward(randint(0, 10))
        if racer.xcor() > 460:
            winner = racer.color()
            is_race_start = False
            break
print(f"Winner is {winner}")
screen.exitonclick()
