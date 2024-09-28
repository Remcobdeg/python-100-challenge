#turtle race

import turtle as t
import random

screen = t.Screen()
screen.setup (width=500, height=300)

choice = screen.textinput("Choose your bet", "Which turtle color do you bet on? (red, blue, green, "
                                             "yellow, purple, or orange) ").lower()

turtles = []

colors = ['red','blue','green','yellow','purple','orange']

game_on = True

for i in range(len(colors)):
    new_turtle = t.Turtle(shape='turtle')
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.setx(-230)
    new_turtle.sety(-100+i*30)
    turtles.append(new_turtle)

while game_on:
    #move turtles forward at random speeds
    for turtle in turtles:
        turtle.forward(random.randint(1,10))
        if turtle.position()[0] >= 230:
            game_on = False
            if turtle.pencolor() == choice:
                print("You won!")
            else:
                print(f"You loose. {turtle.pencolor()} won!")













screen.exitonclick()