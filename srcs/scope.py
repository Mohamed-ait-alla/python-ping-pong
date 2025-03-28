from turtle import Turtle

class Scope(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(350, -200)
        self.pendown()
        for i in range(1, 5):
            self.left(90)
            self.forward(700) if (i % 2 == 0) else self.forward(400)
        self.penup()
        self.goto(0, -200)
        self.pendown()
        self.left(90)
        self.forward(400)
        self.penup()
        self.goto(27, 0)
        self.pendown()
        for _ in range(1, 360):
            self.left(1)
            self.forward(0.5)
        self.penup()
        self.goto(0, -230)
        self.pendown()
        self.color("cyan")
        self.write("made with ❤ by M.H.D.O  © 2025", align="center", font=("courier", 14, "italic", "bold"))
""

