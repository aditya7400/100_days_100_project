from turtle import Turtle,Screen
from time import  sleep
from snake import SnakeBody
from food_obj import FoodObject
from score_board import ScoreBoard

screen = Screen()
screen.tracer(0)
screen.setup(width=600,height=600)
screen.title("SNAKE GAME")
screen.bgpic(picname="snake_bg.png")
score_board = ScoreBoard()
my_snake = SnakeBody()

screen.listen()
game_is_on = True

screen.onkeypress(fun=my_snake.up,key="w")
screen.onkeypress(fun=my_snake.down,key="s")
screen.onkeypress(fun=my_snake.right,key="d")
screen.onkeypress(fun=my_snake.left,key="a")
food = FoodObject()
snake_head = my_snake.my_list[0]
score_board.show_score()


def eat_food():
        if snake_head.distance(food) < 25:
            food.change_pos()
            score_board.score_increase()
            my_snake.increase_length()



while game_is_on:


    sleep(0.25)
    eat_food()

    my_snake.move()
    score_board.show_score()
    if my_snake.check_collision() or my_snake.check_self_collision():
        my_snake.reset_snake()
        snake_head = my_snake.my_list[0]
        score_board.reset_score()

    screen.update()
# my_snake.move_forward()



















screen.exitonclick()