from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.speed("fastest")
        self.penup()
        self.shapesize(1,1)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        #  changed direction
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0,0)
        # self.ball_speed *= 0.1
        self.bounce_x()