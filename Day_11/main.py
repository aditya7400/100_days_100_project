
from turtle import Screen


from score_board import ScoreBoard
from car import Car

from player import Player
screen = Screen()
screen.setup(600,600)
screen.title("Car Game")
screen.listen()
screen.tracer(0)
turtle = Player()
speed = 0.09
car_list = []
for i in range(20):
    car = Car()
    car_list.append(car)
change = 20
for i in car_list[:10]:
    i.setx(300+change)
    change+=100


score_board = ScoreBoard()
screen.onkey(fun=turtle.move_up,key="w")
screen.onkey(fun=turtle.move_down,key="s")
game_is_on = True
while game_is_on:
    # sleep(0.4)
    for i in car_list:
        i.move(speed)
        if i.distance(turtle) < 40: #collision check
            game_is_on = False
            score_board.game_over()
        if i.xcor() <-340:
            i.random_position()
            i.random_color()
    screen.update()

    if turtle.ycor() > 270: #setting turtle back to it's position
        turtle.goto(0,-280)
        score_board.level_up()
        score_board.update_level()
        speed+=0.03























screen.exitonclick()