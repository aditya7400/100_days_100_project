from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.goto(position)
        self.speed("fastest")

        # self.speed("slowest")
    def up(self):
        if 240 > self.ycor():
            self.sety(self.ycor() + 50)

    def down(self):
        if -240 < self.ycor():
            self.sety(self.ycor() - 50)


