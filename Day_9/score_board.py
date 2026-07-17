from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):

        super().__init__()
        self.score = 0

        # self.show.color("red")
        self.speed("fastest")
        self.penup()
        self.hideturtle()
        self.goto(-250, 250)
    def game_over(self):
        self.goto(0,0)
        self.write(arg="Game Over", move=True, align="center", font=('Arial', 20, 'bold'))
    def show_score(self):
        self.clear()
        self.goto(-250, 250)
        self.write(arg=f"Score : {self.score}", move=True, align="left", font = ("Arial", 20, "bold"))
        # self.show.reset()
    def score_increase(self):
        self.score+=1
