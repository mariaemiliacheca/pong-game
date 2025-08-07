import time
from turtle import Screen

from paddle import Paddle
from ball import Ball
from score import Score


#TODO: create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle(350,0)
left_paddle = Paddle(-350,0)
pong_ball = Ball()
scoreboard = Score()

#TODO: create and move a paddle
screen.listen()
screen.onkey(right_paddle.up, key="Up")
screen.onkey(right_paddle.down, key="Down")
screen.onkey(left_paddle.up, key="w")
screen.onkey(left_paddle.down, key="s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    pong_ball.move()

    #TODO: detect collision with wall and bounce
    if pong_ball.ycor() > 299 or pong_ball.ycor() < -299:
        pong_ball.bounce_y()

    #TODO: detect collision with right_paddle
    if (pong_ball.distance(right_paddle) < 50 and pong_ball.xcor() > 320 or
            pong_ball.distance(left_paddle) < 50 and pong_ball.xcor() < -320) :
        pong_ball.bounce_x()

    #TODO: detect when paddle misses
    # right paddle misses
    if pong_ball.xcor() > 380:
        pong_ball.reset_position()
        scoreboard.increase_left_score()

    if pong_ball.xcor() < -380:
        pong_ball.reset_position()
        scoreboard.increase_right_score()

screen.exitonclick()