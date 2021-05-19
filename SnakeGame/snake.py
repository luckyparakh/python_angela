from turtle import Turtle

DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


def create_segment(x):
    tim = Turtle("square")
    tim.penup()
    tim.setpos(x, 0)
    tim.color("white")
    return tim


class Snake:
    x = 0

    def __init__(self):
        self.segment = []
        self.add_segment(20)
        self.head = self.segment[0]

    def add_segment(self, len_seg=1):
        for i in range(len_seg):
            self.segment.append(create_segment(Snake.x))
            Snake.x -= 20

    def movement(self):
        for seq_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seq_num - 1].xcor()
            new_y = self.segment[seq_num - 1].ycor()
            self.segment[seq_num].setpos(new_x, new_y)
        self.head.fd(DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def hit_segment(self):
        flag = False
        for segment in self.segment[1:]:
            if self.head.distance(segment) < 10:
                flag = True
                break
        return flag
