from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.r_score = 0
        self.l_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(x=60, y=200)
        self.write(arg=self.r_score, font=("Arial", 80, 'bold'))
        self.goto(x=-100, y=200)
        self.write(arg=self.l_score, font=("Arial", 80, 'bold'))
