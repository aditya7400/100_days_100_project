from turtle import  Turtle
from random import randint
# from main import my_snake, snake_head
class FoodObject(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.color("yellow")
        self.penup()
        self.change_pos()
        self.speed("fastest")



        # self.my_food = Turtle("circle")
        # self.my_food.color("yellow")
        # self.my_food.penup()
        # self.my_food.goto(x=randint(-280, 280), y=randint(-280, 280))

    def change_pos(self):
        self.goto(x=randint(-280, 280), y=randint(-280, 280))

    # def eat_food(self):
    #     x_snake_head = int(snake_head.xcor())
    #     y_snake_head = int(snake_head.ycor())
    #     x_food_range = range(int(self.my_food.xcor()) - 30, int(self.my_food.xcor()) + 30)
    #     y_food_range = range(int(self.my_food.ycor()) - 30, int(self.my_food.ycor()) + 30)
    #     if x_snake_head in x_food_range and y_snake_head in y_food_range:
    #         my_snake.increase_length()
    #         self.change_pos()
    #         return True
    #     return False

