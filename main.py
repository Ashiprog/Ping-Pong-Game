from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from partition import Partition
import time
my_screen = Screen()
my_screen.bgcolor("black")
my_screen.screensize(canvwidth=800, canvheight=600)
my_screen.title("THE PING PONG GAME")
my_screen.tracer(0)
paddle_1 = Paddle((350, 0))
paddle_2 = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
partition = Partition()
game_is_on = "true"
my_screen.listen()
my_screen.onkey(fun=paddle_1.move_up, key="Up")
my_screen.onkey(fun=paddle_1.move_down, key="Down")
my_screen.onkey(fun=paddle_2.move_up, key="w")
my_screen.onkey(fun=paddle_2.move_down, key="s")
while game_is_on:
    time.sleep(0.2)
    my_screen.update()
    ball.move_ball()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if (ball.distance(paddle_1) < 50 and ball.xcor() > 330) or (ball.distance(paddle_2) < 50 and ball.xcor() < -330):
        ball.bounce_x()
    if ball.xcor() > 390:
        ball.refresh()
        scoreboard.increase_score_left()
        ball.bounce_x()
    if ball.xcor() < -390:
        ball.refresh()
        scoreboard.increase_score_right()
        ball.bounce_x()
my_screen.exitonclick()