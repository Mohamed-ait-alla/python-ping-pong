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

screen.exitonclick()