import turtle as t
import time
from snake import Snake

#set up the screen
screen = t.Screen()
screen.setup(width=600, height=600)
screen.title("Snake game")
screen.bgcolor('black')
screen.tracer(0) #this now gives us control to determine when to update the screen

game_on = True

snake = Snake()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")




while game_on:
    screen.update()
    time.sleep(.1)
    snake.move()



screen.exitonclick()
