import time
import turtle

from ball import Ball
from paddle import Paddle

turtle.title("Pong")
turtle.bgcolor('black')
turtle.setup(width=800, height=600)
turtle.tracer(n=0)

r_paddle = Paddle((370, 0))
l_paddle = Paddle((-370, 0))

ball = Ball()

turtle.listen()
turtle.onkeypress(fun=r_paddle.up, key="Up")
turtle.onkeypress(fun=r_paddle.down, key="Down")
turtle.onkeypress(fun=l_paddle.up, key="w")
turtle.onkeypress(fun=l_paddle.down, key="s")

while True:
    ball.move()
    if ball.ycor() > 280:
        ball.move(ysteps=-10)
    turtle.update()
    time.sleep(0.1)
