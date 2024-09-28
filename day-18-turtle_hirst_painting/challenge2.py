from turtle import Turtle, Screen
from random import choice

turtle = Turtle()
screen = Screen()
screen.colormode(255)
turtle.shape('turtle')
turtle.penup()
turtle.speed(0)

colors = [(212, 155, 107), (214, 232, 240), (46, 110, 144), (124, 172, 196), (197, 135, 158), (145, 71, 93), (232, 202, 111), (43, 129, 98), (153, 81, 62), (190, 92, 116), (128, 181, 158), (204, 91, 72), (58, 163, 133), (153, 159, 60), (52, 157, 178), (229, 166, 183), (234, 171, 159), (150, 210, 220), (152, 213, 201), (19, 94, 69), (46, 57, 97), (31, 53, 81), (115, 116, 159), (94, 48, 65), (63, 44, 60), (21, 66, 44), (180, 186, 214)]

size = 10
jump = 50

# turtle.position(20,20)

turtle.setx(-200)

for h in range(10):
    turtle.sety(-200)
    turtle.setx(turtle.position()[0] + 50)

    for v in range(10):
        turtle.dot(size,choice(colors))
        turtle.sety(turtle.position()[1]+50)








screen.exitonclick()