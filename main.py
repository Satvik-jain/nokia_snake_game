from turtle import Screen
import time
from snake import Snake
from food import Food

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Nokia Snake Game")
screen.tracer(0)

snake = Snake()

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
    print(snake.head.pos())
    print(eat.food.pos())
    if snake.head.distance(eat.food) < 15:
        snake.add()
        eat.locate()

    screen.update()
    time.sleep(0.08)
    snake.move()

    if snake.head.pos() in [i.pos() for i in snake.segments[1:]]:
        is_game_on = False

    is_game_on = snake.check_wall()

screen.exitonclick()
