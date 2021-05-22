from turtle import Turtle
from random import randint


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.setpos(0, 0)
        self.x_offset = 5
        self.y_offset = 5
        self.move_speed = 0.1
        self.penup()

    def movement(self):
        self.setpos(self.xcor() + self.x_offset, self.ycor() + self.y_offset)

    def bounce_y(self):
        # To bounce off the ball, change the speed vector of ball from positive to negative along axis where
        # ball will need to bounce off.
        # If ball wants to bounce Y axis then change speed of Y component.
        # Let say ball is travelling like (1,1) -> (2,2) -> (3,3) -> (4,4) and wall is at Y = 5.
        # To bounce it back reverse speed direction ie instead of adding the offset , subtract the offset.
        # Now ball will travel like (5,3) -> (6,2) -> (7,1).
        # In other way, ball should not cross Y = 5 or Y = -5, so to stop that decrease Y coordinate or increase
        # Y coordinate respectively.
        self.y_offset *= -1

    def bounce_x(self):
        self.x_offset *= -1
        # To increase speed reduce sleep time.
        self.move_speed *= 0.9

    def reset(self):
        self.setpos(0, 0)
        self.move_speed = 0.1
        # To move ball in opposite direction so that another player get chance.
        self.x_offset *= -1
