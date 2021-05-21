from turtle import Turtle


class Pedestrian(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setpos(0, -260)
        self.shape("turtle")
        self.setheading(90)

    def move(self):
        self.fd(10)
