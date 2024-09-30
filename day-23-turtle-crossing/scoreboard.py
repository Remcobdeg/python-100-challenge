FONT = ("Courier", 24, "normal")

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        # self.level = 0
        self.write_score(0)

    def write_score(self,level):
        self.goto(-250,260)
        self.clear()
        self.write(f"Level: {level}",font=FONT)

    # def increase_level(self):
    #     self.level += 1
    #     self.write_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",font=FONT)

