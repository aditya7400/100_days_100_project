from turtle import Turtle
class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pensize(5)
        self.color("white")
        self.goto(0,-300)
        self.goto(0,300)

