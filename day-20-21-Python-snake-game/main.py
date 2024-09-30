import turtle as t
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

#set up the screen
screen = t.Screen()
screen.setup(width=600, height=600)
screen.title("Snake game")
screen.bgcolor('black')
screen.tracer(0) #this now gives us control to determine when to update the screen

game_on = True

snake = Snake()
food = Food()
board = ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")




while game_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    #Detect distance from food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        board.update_score()

    if (snake.head.position()[0] > 280 or
            snake.head.position()[0] < -280 or
            snake.head.position()[1] < -280 or
            snake.head.position()[1] > 280):
        board.game_over()
        game_on = False

    #Detect collision head with tail
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            board.game_over()



screen.exitonclick()
