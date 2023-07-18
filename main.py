from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Nokia Snake Game")
screen.tracer(0)

snake = Snake()

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()
