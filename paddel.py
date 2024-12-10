from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("red")
        self.goto(position)
        self.shapesize(5, 1)
    
    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 10)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 10)