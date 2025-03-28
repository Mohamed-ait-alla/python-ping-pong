from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("yellow")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_left_score(self):
        self.l_score += 1
        self.update_scoreboard()

    def update_right_score(self):
        self.r_score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 230)
        self.write("score", align="center", font=("courier", 18, "bold"))
        self.goto(-50, 205)
        self.write(self.l_score, align="center", font=("courier", 16, "bold"))
        self.goto(0, 205)
        self.color("white")
        self.write("|", align="center", font=("courier", 18, "bold"))
        self.color("yellow")
        self.goto(50, 205)
        self.write(self.r_score, align="center", font=("courier", 16, "bold"))
    
