from turtle import Turtle ,Screen
screen = Screen()


from Day_6.font_list import my_list

STARTING_POSITON = [(0,0),(0,-20),(0,-40)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class SnakeBody:

    def __init__(self):

        self.my_list = []


        for coordinates in STARTING_POSITON:
            snake = Turtle("square")
            snake.color("black")
            snake.speed("fastest")
            snake.penup()
            snake.goto(coordinates)
            self.my_list.append(snake)
        self.snake_head = self.my_list[0]


    def follow_snake(self):

        for i in range(len(self.my_list)-1,0,-1):
            x_cor = self.my_list[i-1].xcor()
            y_cor = self.my_list[i - 1].ycor()
            self.my_list[i].goto(x_cor,y_cor)

    def move(self):

        # position = self.my_list[0].pos()
        self.follow_snake()
        self.snake_head.forward(20)

    def increase_length(self):
        snake_block = Turtle("square")
        snake_block.penup()
        # snake_block.shape("square")
        self.my_list.append(snake_block)
        
    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(90)
    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(270)
    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(0)
    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(180)
    def check_self_collision(self):
        head_pos = self.snake_head.pos()
        tail = self.my_list[1:]
        for tail_block in tail:
            tail_block_pos = tail_block.pos()
            if head_pos[0] == tail_block_pos[0] and head_pos[1] == tail_block_pos[1]:
                return True
        return False

    def check_collision(self):
        x_snake_head = int(self.snake_head.xcor())
        y_snake_head = int(self.snake_head.ycor())
        allowed = range(-290, 291)
        if x_snake_head not in allowed or y_snake_head not in allowed:
            return True
        return False











