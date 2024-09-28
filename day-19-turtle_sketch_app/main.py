import turtle as t

turtle = t.Turtle()
screen = t.Screen()

def forward():
    turtle.forward(5)

def right():
    turtle.right(5)

def left():
    turtle.left(5)

def backward():
    turtle.backward(5)

def clean_screen():
    screen.reset()


turtle.speed(9)

screen.listen()
screen.onkey(forward,"w")
screen.onkey(right,"s")
screen.onkey(left,"a")
screen.onkey(backward,"d")
screen.onkey(clean_screen,"c")






screen.exitonclick()