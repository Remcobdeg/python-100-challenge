from turtle import Turtle

ALIGN="center"
FONT=('Arial', 10, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,280)
        self.write_score()

    def write_score(self):
        self.clear()  # remove previous writing
        self.write(arg=f"Score: {self.score} High Score: {self.highscore}",align=ALIGN,font=FONT)

    def update_score(self):
        self.score += 1
        self.write_score()

    def reset(self):
        # replacing game over def
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt",mode="w") as file:
                file.write(str(self.highscore))

        self.score = 0
        self.write_score()



    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER",align=ALIGN,font=FONT)
