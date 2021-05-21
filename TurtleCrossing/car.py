from turtle import Turtle
from random import randint, choice

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


class Car(Turtle):
    car_speed = 5

    def __init__(self):
        super(Car, self).__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=2,stretch_wid=0.5)
        self.setpos(250, randint(-220, 220))
        self.setheading(180)
        self.color(choice(colors))

    def move(self):
        self.fd(Car.car_speed)


