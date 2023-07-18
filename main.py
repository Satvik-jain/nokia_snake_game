from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Nokia Snake Game")
screen.tracer(0)

starting_position = [(0,0),(-20,0),(-40,0)]

segments = []

for position in starting_position:
    new = Turtle('square')
    new.color('white')
    new.penup()
    new.goto(position)
    segments.append(new)

screen.update()

is_game_on =True


while is_game_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(segments) - 1,0,-1):
        new_x = segments[seg_num-1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x,new_y)
    segments[0].forward(20)

screen.exitonclick()