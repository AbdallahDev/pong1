import time
import turtle

from ball import Ball
from net import Net
from paddle import Paddle
from score_board import ScoreBoard

turtle.title("Pong")
turtle.bgcolor('black')
turtle.setup(width=800, height=600)
turtle.tracer(n=0)

net = Net()
r_paddle = Paddle((370, 0))
l_paddle = Paddle((-370, 0))
ball = Ball()

score_board = ScoreBoard()

turtle.listen()
turtle.onkeypress(fun=r_paddle.up, key="Up")
turtle.onkeypress(fun=r_paddle.down, key="Down")
turtle.onkeypress(fun=l_paddle.up, key="w")
turtle.onkeypress(fun=l_paddle.down, key="s")

while True:
    ball.move()

    print(ball.xcor(), ball.ycor(), ball.distance(r_paddle))
    if ball.xcor() > 400:
        score_board.l_score += 1
        score_board.update_score()
        ball.reset_()
    elif ball.xcor() < -400:
        score_board.r_score += 1
        score_board.update_score()
        ball.reset_()

    if (ball.xcor() >= 345 and ball.distance(r_paddle) < 45 and ball.x_steps >= 0) or (
            ball.xcor() < -345 and ball.distance(l_paddle) < 45 and ball.x_steps < 0):
        ball.x_bounce()

    turtle.update()
    time.sleep(ball.time)
