from turtle import Turtle
class Scoreboard(Turtle):

    def __init__(self,x_cor,y_cor,color):
        super().__init__()
        self.penup()
        self.setpos(x_cor,y_cor)
        self.hideturtle()
        self.pencolor(color)
        self.score = 0
        self.write(f"{self.score}",False,"center",("Comic Sans MS",50,"normal"))

    def point(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", False,"center", ("Comic Sans MS", 50, "normal"))

    def winner_blue(self):
        self.setpos(0, -150)
        self.write("   Mavi\nKazandı!", False, "center", ("Comic Sans MS", 90, "normal"))

    def winner_red(self):
        self.setpos(0, -150)
        self.write(" Kırmızı\nKazandı!", False, "center", ("Comic Sans MS", 90, "normal"))