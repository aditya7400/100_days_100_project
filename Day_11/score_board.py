from turtle import Turtle



class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-240,265)
        self.level = 1
        self.update_level()
    def update_level(self):
        self.clear()
        self.write(f"level: {self.level}",align="center",font=("Courier", 15, "bold"))
    def level_up(self):
        self.level+=1
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=("Courier", 30, "bold"))
