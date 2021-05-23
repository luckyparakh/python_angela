from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 285)
        self.color("white")
        self.hideturtle()

    def write_score(self):
        self.clear()
        self.write(f'Score: {self.score}')
        self.score += 1