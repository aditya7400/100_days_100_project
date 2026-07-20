from turtle import Screen

from Day_10.line import Line
from score_board import ScoreBoard
from paddle import Paddle
from ball import Ball

POSITION_LEFT = (-350,0)
POSITION_RIGHT = (350,0)
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
right_paddle = Paddle(POSITION_RIGHT)
left_paddle = Paddle(POSITION_LEFT)
ball = Ball()
score_board = ScoreBoard()
line = Line()

screen.update()
screen.listen()

screen.onkey(fun=right_paddle.up, key="w")
screen.onkey(fun=right_paddle.down, key="s")
screen.onkey(fun=left_paddle.up,key="Up")
screen.onkey(fun=left_paddle.down,key="Down")
print(left_paddle.xcor())
while True:
    if -380>ball.xcor():
        ball.reset_position()
        score_board.r_point()
    if 380<ball.xcor():
        ball.reset_position()
        score_board.l_point()



    ball.ball_move()
    screen.update()

    if int(ball.ycor())<-280 or int(ball.ycor()) > 280:
        ball.bounce_y()

    if ball.distance(right_paddle)<50 and ball.xcor()>330 :

        ball.bounce_x()
        ball.setx(330)
        ball.speed_up()
    if ball.distance(left_paddle)<50 and ball.xcor()<-330:
        ball.bounce_x()
        ball.setx(-330)
        ball.speed_up()












screen.exitonclick()