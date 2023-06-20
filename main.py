from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=600,width=800)
screen.bgcolor("grey")
screen.title("Pong Game")

screen.tracer(0)
p1 = Paddle(-350,0,"blue4")
p2 = Paddle(350,0,"red4")
ball = Ball()
score1 = Scoreboard(-100,220,"blue2")
score2 = Scoreboard(100,220,"red2")

screen.listen()

screen.onkey(key="w", fun=p1.go_up)
screen.onkey(key="s", fun=p1.go_down)
screen.onkey(key="Up", fun=p2.go_up)
screen.onkey(key="Down", fun=p2.go_down)


gaming = True
while gaming:
    ball.move()
    # ball hits a wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.change_direction()
    # ball hits a player
    if abs(ball.xcor() - p1.xcor()) < 20 and abs(ball.ycor() - p1.ycor()) < 55:
        ball.change_direction()
    if abs(ball.xcor() - p2.xcor()) < 20 and abs(ball.ycor() - p2.ycor()) < 55:
        ball.change_direction()
    # player misses the ball
    if ball.xcor() > 400:
        score1.point()
        ball.reset_ball()
    elif ball.xcor() < -400:
        score2.point()
        ball.reset_ball()

    screen.update()

screen.exitonclick()