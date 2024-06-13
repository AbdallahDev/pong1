from turtle import Turtle


class Net(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(x=0, y=300)
        self.pendown()
        self.goto(x=0, y=-300)
