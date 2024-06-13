from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_steps = 10
        self.y_steps = 10
        self.time = 0.1

    def move(self):
        self.goto(self.xcor() + self.x_steps, self.ycor() + self.y_steps)
        if self.ycor() > 280 or self.ycor() < -280:
            self.y_bounce()

    def y_bounce(self):
        self.y_steps *= -1

    def x_bounce(self):
        self.accelerate()
        self.x_steps *= -1

    def accelerate(self):
        self.time -= 0.01

    def reset_(self):
        self.time = 0.1
        self.goto(0, 0)
        self.x_bounce()
