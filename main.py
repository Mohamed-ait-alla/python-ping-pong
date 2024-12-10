from turtle import Screen, Turtle
from paddel import Paddle
from ball import Ball

screen = Screen()
screen.title("Ping pong game")
screen.bgcolor("black")
screen.screensize(600, 600)

right_paddle = Paddle((240,0))
left_paddle = Paddle((-240,0)) 
ball = Ball()


screen.listen()

screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_on = True
while game_on:
    ball.goto(ball.xcor() + 1, ball.ycor() + 1)
screen.exitonclick()