from turtle import Turtle
from  random import randint as r

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("black")
        self.penup()
        self.setheading(r(15,45))
        self.ball_speed = 0.1

    def move(self):
        self.forward(self.ball_speed)

    def change_direction(self):
        self.setheading(self.heading() - r(30,90))
        self.ball_speed += 0.001

    def reset_ball(self):
        self.setpos(0,0)
        self.ball_speed = 0.1
        self.setheading(self.heading() + 180)

