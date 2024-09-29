from turtle import Turtle

ALIGN = "center"
FONT = ('Courier',80,"normal")

class Scoreboard(Turtle):
    def __init__(self, x_position):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(x_position,200)
        self.show_score()

    def count_point(self):
        self.score += 1
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(self.score,align=ALIGN,font=FONT)

