from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        # self.xstep = 10
        # self.ystep = 10

    def move(self, xsteps=10, ysteps=10):
        self.goto(self.xcor() + xsteps, self.ycor() + ysteps)
