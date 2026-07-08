from itertools import count
from turtle import Turtle, Screen, colormode
from random import choice
# import colorgram as c

# color = c.extract("dot_painting.jpg", 34)
color_pallet = [ (208, 160, 82), (54, 89, 131),
                (146, 91, 40), (140, 26, 48), (222, 206, 108), (132, 177, 203), (158, 45, 83), (47, 55, 103),
                (167, 160, 38), (128, 189, 143), (84, 20, 44), (36, 42, 70), (187, 93, 105), (187, 139, 170),
                (84, 123, 181), (59, 39, 31), (78, 153, 165), (88, 157, 91), (195, 79, 72), (45, 74, 78),
                (161, 202, 220), (80, 73, 44), (57, 131, 121), (218, 176, 188), (220, 183, 166), (166, 207, 165),
                (179, 188, 211), (149, 37, 35), (46, 73, 71), (45, 65, 62)]

# for obj in color:
#     r = obj.rgb.r
#     g = obj.rgb.g
#     b = obj.rgb.b
#     color_tuple = (r, g, b)
#     color_pallet.append(color_tuple)

colormode(255)
dot = Turtle()
dot.speed("fastest")
dot.teleport(-225,-225)
dot.shape("circle")
dot.penup()
index = 0
for _ in range(10):
    for i in range(10):
        dot.color(color_pallet[index%len(color_pallet)])
        dot.stamp()
        dot.forward(50)
        index+=1

    dot.teleport(-225,dot.ycor()+50)
dot.hideturtle()
print(color_pallet)

screen = Screen()
screen.exitonclick()
