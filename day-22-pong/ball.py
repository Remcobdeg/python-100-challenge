from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.color("white")
        self.penup()
        self.setheading(45)

    def move(self):
        self.forward(10)

    def bounce(self):
        self.setheading(-self.heading())

    def bounce_paddle(self):
        self.setheading(180-self.heading())