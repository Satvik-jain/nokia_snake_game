from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Nokia Snake Game")
screen.tracer(0)


snake = Snake()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True

eat = Food()
while True:
    if eat.food.pos() != (0, 0):
        break

while is_game_on:
    if snake.head.distance(eat.food) < 15:
        snake.add()
        eat.locate()
        scoreboard.add_score()
        scoreboard.refresh()

    screen.update()
    time.sleep(0.08)
    snake.move()

    for snake_Part in [i for i in snake.segments[3:]]:
        print(snake_Part)
        if  snake.head.distance(snake_Part) < 10:
            is_game_on = False
            break

    if is_game_on:
        is_game_on = snake.check_wall()

    if is_game_on == False:
        scoreboard.gameover()

screen.exitonclick()
