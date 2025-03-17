from turtle import Screen, Turtle
from paddel import Paddle
from ball import Ball
from score import Scoreboard
import time

screen = Screen()

screen.title("Ping pong game")
screen.bgcolor("black")
screen.screensize(600, 600)
screen.tracer(0)

right_paddle = Paddle((240,0))
left_paddle = Paddle((-240,0)) 
ball = Ball()
scoreboard = Scoreboard()
 
screen.listen()
screen.tracer(0)

screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

default_speed = 0.1
game_on = True
while game_on:
    screen.update()
    time.sleep(default_speed)
    ball.goto(ball.xcor() + ball.x_move, ball.ycor() + ball.y_move)
    # when it crashes the up or down wall
    if (ball.ycor() <= -210 or ball.ycor() >= 210):
        ball.y_move *= -1
    # when it get close to one the paddles
    if ((ball.xcor() <= -220 and ball.distance(left_paddle) <= 50) or (ball.xcor() >= 220 and ball.distance(right_paddle) <= 50)):
        ball.x_move *= -1
        default_speed *= 0.9
    # when it goes arround toward right side
    if (ball.xcor() > 280):
        ball.goto(0, 0)
        ball.x_move *= -1
        default_speed = 0.1
        scoreboard.update_left_score()
    # when it goes arround toward left side
    if (ball.xcor() < -280):
        ball.goto(0, 0)
        ball.x_move *= -1
        default_speed = 0.1
        scoreboard.update_right_score()
    
screen.exitonclick()