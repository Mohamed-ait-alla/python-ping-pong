from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.penup()
        self.goto(0,0)
        self.color("white")
        self.x_move = 10
        self.y_move = 10