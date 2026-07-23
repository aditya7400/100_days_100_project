import turtle
from write import Write
from data_process import give_cor
pen = Write()
screen = turtle.Screen()
screen.title("India States Game")
screen.setup(600,697)
screen.bgpic("map.gif")
def take_input():
    ans = screen.textinput(title=f"Guessed states :{pen.guessed_out_of_30}/30",prompt="Enter a state name")
    if ans:
        ans = ans.title()
    return ans
game_is_on = True
def get_mouse_click_coor(x,y):
   print(x , y)
turtle.onscreenclick(get_mouse_click_coor)
while game_is_on:
    state_name = take_input()

    cor = give_cor(state_name)
    if cor:
        pen.guessed_out_of_30+=1
        pen.state_name(cor[0],cor[1],state_name)
    if pen.guessed_out_of_30 == 30:
        game_is_on = False
        pen.goto(0,0)
        pen.write("You Won",align="center",font=("Courier", 70, "normal"))


turtle.mainloop()



