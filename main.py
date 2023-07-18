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
    for seg in segments:
        seg.forward(20)



screen.exitonclick()
