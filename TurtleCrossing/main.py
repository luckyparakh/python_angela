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
from TurtleCrossing.scoreboard import ScoreBoard

is_game_on = True
screen = Screen()
screen.setup(560, 560)
screen.title("Road Crossing Game")
screen.tracer(0)
screen.listen()
walker = Pedestrian()
sb = ScoreBoard()
sb.write_score()
screen.onkeypress(walker.move, "Up")
car_obj = Car()

while is_game_on:
    screen.update()
    sleep(0.1)

    if walker.ycor() > 245:
        pass
        walker.reset_pos()
        sb.write_score()
        Car.car_speed += 1

    for car in car_obj.cars:
        car_obj.move_car(car)
        car_obj.remove_car(car)
        if car.distance(walker) < 15:
            walker.reset_pos()
            is_game_on = False
            sb.game_over()

    car_obj.add_car()


screen.exitonclick()
