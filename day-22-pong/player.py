from turtle import Turtle

class Player(Turtle):
    def __init__(self,x_position=350):
        super().__init__()
        #build the paddle
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        #position the paddle
        self.penup()
        self.speed(0)
        self.goto((x_position,0))

    def up(self):
        new_y = self.ycor()+10
        self.sety(new_y)

    def down(self):
        new_y = self.ycor()-10
        self.sety(new_y)

