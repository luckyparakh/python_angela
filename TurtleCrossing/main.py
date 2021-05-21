"""
a. Create a screen
b. Create turtle & add key to it.
c. Add cars & make those move randomly.
d. Collision detection & game over.
e. End of screen detection & increase speed of cars & reset turtle.
f. Create Scoreboard.

"""

from turtle import Screen
from TurtleCrossing.pedestrian import Pedestrian
from TurtleCrossing.car import Car
from time import sleep

is_game_on = True
screen = Screen()
screen.setup(560, 560)
screen.title("Road Crossing Game")
screen.tracer(0)
screen.listen()
walker = Pedestrian()
screen.onkeypress(walker.move, "Up")
cars = []

while is_game_on:
    screen.update()
    sleep(0.1)
    cars.append(Car())
    for car in cars:
        if car.xcor() < -300:
            cars.remove(car)
        car.move()

screen.exitonclick()
