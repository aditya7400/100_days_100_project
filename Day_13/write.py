from turtle import Turtle,Screen
class Write(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.guessed_out_of_30 =0


    def state_name(self,x,y,name):
        self.goto(x,y)
        self.write(name,align="center",font=("Courier", 10, "normal"))


