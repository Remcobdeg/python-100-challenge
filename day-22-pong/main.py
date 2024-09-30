#TODO: 1 create board + line
from screen import Line
from turtle import Screen
from player import Player
from ball import Ball
from scoreboard import Scoreboard
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
ball = Ball()
scoreboard1 = Scoreboard(x_position = 100)
scoreboard2 = Scoreboard(x_position = -100)


screen.listen()
screen.onkey(player2.up,"d")
screen.onkey(player2.down,"a")
screen.onkey(player1.up,"l")
screen.onkey(player1.down,"j")

speed=10
game_on = True

while game_on:
    #bounce off wall
    time.sleep(1/speed)
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce()

    #bounce off paddle
    if (ball.xcor() >= 330 and ball.distance(player1) <= 50) or (ball.xcor() <= -330 and ball.distance(player2) <= 50):
        ball.bounce_paddle()
        speed *= 1.5

    #score player2
    if ball.xcor() > 380:
        ball.home()
        ball.setheading(45+180)
        scoreboard2.count_point()
        speed=10

    #score player1
    if ball.xcor() < -380:
        ball.home()
        ball.setheading(45)
        scoreboard1.count_point()
        speed=10

    ball.move()
    screen.update()

screen.exitonclick()

