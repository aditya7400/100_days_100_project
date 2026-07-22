from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):

        super().__init__()
        self.score = 0
        # self.high_score = 0
        with open("data.txt" , mode="r") as file:
            self.high_score = int(file.read())
        # self.show.color("red")
        self.speed("fastest")
        self.penup()
        self.hideturtle()
        self.goto(-250, 250)
    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt",mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0

    def show_score(self):
        self.clear()
        self.goto(-250,250)
        self.write(arg=f"Score : {self.score}  High Score : {self.high_score}", move=True, align="left", font = ("Arial", 20, "bold"))
        # self.show.reset()

    def score_increase(self):
        self.score+=1
