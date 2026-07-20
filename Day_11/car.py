
from turtle import Turtle, colormode
from random import randint,choice

colormode(255)

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=2,stretch_len=3)
        self.random_color()
        self.x_list = list(range(400,3000,70))
        self.y_list = list(range(-250,250,50))
        self.random_position()

    def random_color(self):
        r = randint(0,255)
        g = randint(0,255)
        b = randint(0,255)
        self.color(r,g,b)
    def random_position(self):
        x_cor = choice(self.x_list)
        y_cor = choice(self.y_list)
        self.goto(x_cor,y_cor)
    def move(self,speed):
        self.backward(speed)

