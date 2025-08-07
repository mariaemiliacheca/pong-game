from turtle import Turtle

class Score(Turtle):
    def __init__(self):
       super().__init__()
       self.left_score = 0
       self.right_score = 0
       self.penup()
       self.color("white")
       self.hideturtle()
       self.update_scoreboard()

    def update_scoreboard(self):
       self.clear()
       self.goto(-100,200)
       self.write(self.left_score, align="center", font=("Courier", 60, "normal"))
       self.goto(100,200)
       self.write(self.right_score, align="center", font=("Courier", 60, "normal"))

    def increase_left_score(self):
        self.left_score += 1
        self.update_scoreboard()

    def increase_right_score(self):
        self.right_score += 1
        self.update_scoreboard()
