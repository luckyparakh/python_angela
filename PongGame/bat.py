from turtle import Turtle


class Bat(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.setpos(position)
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.score = 0

    def up(self):
        if self.ycor() < 240:
            self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        if self.ycor() > -240:
            self.goto(self.xcor(), self.ycor() - 20)
