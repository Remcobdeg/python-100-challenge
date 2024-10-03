from turtle import Turtle

class TextTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def writeText(self,text,x,y):
        self.goto(x,y)
        self.write(text)