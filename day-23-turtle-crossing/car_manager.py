
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random

class CarManager:
    def __init__(self):
        self.cars = []

    def add_car(self):
        self.cars.append(Car())

class Car(Turtle):
    def __init__(self):
        super().__init__()
        #set appearance
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.penup()
        #set position and direction
        self.setheading(180)
        self.y = random.randint(-220,290)
        self.goto(310,self.y)


    def move(self):
        self.forward(MOVE_INCREMENT)
