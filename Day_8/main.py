
from turtle import Turtle, Screen
from random import randint



turtle_list = []
color_list = ["red","blue","indigo","green","violet","orange","yellow"]
for i in range (7):
    my_turtle = Turtle()
    turtle_list.append(my_turtle)

index = 0
y_pos = -90
screen = Screen()

screen.setup(width=1000,height=400)
bet_color = screen.textinput(title="Welcome to the Turtle Race",prompt=f"On which turtle you want to bet.\nEnter a color from list\n{color_list} : ")
for turtle in turtle_list:
    turtle.penup()
    turtle.shape("turtle")
    turtle.color(color_list[index])
    turtle.setpos(-450,y_pos)
    y_pos+=40
    index +=1
def random_speed(turtle_obj):
    steps = randint(3,13)
    turtle_obj.forward(steps)
def check_win(turtle_obj):
    if turtle_obj.xcor() > 480:
        return turtle_obj.color()[0]
    return "not end"

while True:
    for turtle in turtle_list:
        winner = check_win(turtle)
        if winner in color_list:
            if winner == bet_color:
                print("Congratulation You Won")
            else:
                print(f"Damn You lost\nBetter luck next time")
            screen.exitonclick()
            break

        else:

            random_speed(turtle_obj=turtle)






