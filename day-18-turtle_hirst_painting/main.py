from random import sample
from turtle import Turtle, Screen
import  random

turtle = Turtle()
screen = Screen()
turtle.shape('turtle')
turtle.color('teal')

#turtle challenge 1: square
# for n in range(4):
#     turtle.forward(100)
#     turtle.right(90)

#turtle challenge 2: dashed line
# for n in range(10):
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(10)
#     turtle.pendown()

#turtle challenge 3: polygons (3 to 10 angles), random colours

screen.colormode(255)

def random_color_digit():
    return random.randint(0,255)

def random_color():
    color = []
    for n in range(3):
        color.append(random_color_digit())
    return tuple(color)

# for n_angles in range(3,10):
#     turtle.color(random_color())
#     for i in range(n_angles):
#         turtle.forward(50)
#         turtle.right(360/n_angles)

# turtle challenge 4: random walk
# add thick lines and faster turtle

# walk = True
#
# def stop():
#     global walk
#     walk = not walk
#     print("pressed space")
#
#
# turtle.pensize(10)
# turtle.speed(9)
#
# while walk:
#     turtle.color(random_color())
#     turtle.forward(10)
#     turtle.right(random.choice([0, 90,180,270]))
#
#     screen.onkey(stop, "space")
#     screen.listen()

# turtle challenge 5: spiraling circles

turtle.speed(0)

n_circles = 60

for i in range (n_circles):
    turtle.circle(100)
    turtle.right(360/n_circles)

screen.exitonclick()
