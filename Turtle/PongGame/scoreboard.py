from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.setpos(-50, 285)
        self.color("white")
        self.hideturtle()
        self.lp_score = 0
        self.rp_score = 0

    def write_score(self):
        self.clear()
        self.write(f'Score: LP:{self.lp_score}, RP:{self.rp_score}')
