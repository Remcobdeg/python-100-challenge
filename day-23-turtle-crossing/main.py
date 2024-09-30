from turtle import Screen
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard
import time
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

carStock = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move,"Up")

game_is_on = True
while game_is_on:
    scoreboard.write_score(player.level)
    #add cars
    if random.random() > .90:
        carStock.add_car()
    #move cars and detect collision
    for car in carStock.cars:
        car.move()
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    time.sleep(0.15/player.level*1.5)
    screen.update()

screen.exitonclick()