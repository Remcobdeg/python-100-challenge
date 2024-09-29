#TODO: 1 create board + line
from screen import Line
from turtle import Screen
from player import Player
import time

#setup canvas
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgcolor('black')
screen.tracer(0)  # this now gives us control to determine when to update the screen

#middle line
line = Line()

player1 = Player(x_position=350)
player2 = Player(x_position=-350)

screen.listen()
screen.onkey(player2.up,"d")
screen.onkey(player2.down,"a")
screen.onkey(player1.up,"l")
screen.onkey(player1.down,"j")

game_on = True

while game_on:
    # time.sleep(.01)
    screen.update()

#TODO: 2 create + move player bar
#TODO: 3 create second bar
#TODO: 4 create ball
#TODO: 5 bounce ball on wall
#TODO: 6 bounce ball on paddle
#TODO: 7 detect miss
#TODO: 8 keep score

screen.exitonclick()

