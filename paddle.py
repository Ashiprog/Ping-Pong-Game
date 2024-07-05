from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def move_up(self):
        x_cor = self.xcor()
        new_y = self.ycor() + 10
        self.goto(x_cor, new_y)

    def move_down(self):
        x_cor = self.xcor()
        new_y = self.ycor() - 10
        self.goto(x_cor, new_y)
