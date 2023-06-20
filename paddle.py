from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,x_cor,y_cor,color):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.setpos(x_cor,y_cor)


    def go_up(self):
        self.setpos(self.xcor(), self.ycor() + 20)

    def go_down(self):
        self.setpos(self.xcor(), self.ycor() - 20)