from turtle import Screen, Turtle
from paddel import Paddle
from ball import Ball
import time

screen = Screen()
screen.title("Ping pong game")
screen.bgcolor("black")
screen.screensize(600, 600)
screen.tracer(0)

right_paddle = Paddle((240,0))
left_paddle = Paddle((-240,0)) 
ball = Ball()


screen.listen()
screen.tracer(0)

screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    ball.goto(ball.xcor() + ball.x_move, ball.ycor() + ball.y_move)
    if (ball.ycor() <= -210 or ball.ycor() >= 210):
        ball.y_move *= -1
    if ((ball.xcor() <= -220 and ball.distance(left_paddle) <= 50) or (ball.xcor() >= 220 and ball.distance(right_paddle) <= 50)):
        ball.x_move *= -1
    
screen.exitonclick()