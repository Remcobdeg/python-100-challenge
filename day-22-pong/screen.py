from turtle import Turtle

# class Window(Screen):
#     def __init__(self):
#         super().__init__()
        # #setup canvas
        # self.setup(width=600, height=600)
        # self.title("Pong")
        # self.bgcolor('black')
        # self.tracer(0)  # this now gives us control to determine when to update the screen
        # #setup line
        # # self.Line()


class Line(Turtle):
    def __init__(self):
        super().__init__()
        # self.shape("square")
        self.color("grey")
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.setposition((0, -300))
        self.left(90)
        for y in range(0,600,60):
            self.pendown()
            self.forward(30)
            self.penup()
            self.forward(30)













