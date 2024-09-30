import turtle as t

STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake = []
        self.make_snake()
        self.head = self.snake[0]

    def make_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        segment = t.Turtle(shape="square")
        segment.color('white')
        segment.penup()
        segment.setposition(position)
        self.snake.append(segment)

    def extend(self):
        self.add_segment(self.snake[-1].position())

    def move(self):
        for segment_n in range(len(self.snake)-1,0,-1):
            new_position = tuple(self.snake[segment_n-1].position())
            # noinspection PyTypeChecker
            self.snake[segment_n].setposition(new_position)
        self.head.forward(20)

    def up(self):
        #if moving right or left
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        #move old snake off the screen
        for seg in self.snake:
            seg.goto(1000,1000)
        self.snake.clear()
        self.make_snake()
        self.head = self.snake[0]


