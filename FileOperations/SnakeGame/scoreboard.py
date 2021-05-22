from turtle import Turtle





class ScoreBoard(Turtle):

    @staticmethod
    def read_highest_score():
        with open("score.txt") as file:
            return file.read()

    @staticmethod
    def write_highest_score(hscore):
        with open("score.txt", "w") as file:
            file.write(hscore)

    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 285)
        self.color("white")
        self.hideturtle()
        self.high_score = ScoreBoard.read_highest_score()
        self.write(f'Score: {self.score} Highest: {self.high_score}')

    def write_score(self):
        self.clear()
        self.score += 1
        self.high_score = ScoreBoard.read_highest_score()
        if self.score > int(self.high_score):
            self.high_score = self.score
        self.write(f'Score: {self.score} Highest: {self.high_score}')

    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over')
