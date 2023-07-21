from turtle import Turtle
import snake
from random import randrange


class Food:
    def __init__(self):
        self.food = Turtle()
        self.food.color("red")
        self.food.shape('circle')
        self.food.speed(0)
        self.food.shapesize(0.8, 0.8, 1)
        self.locate()

    def locate(self):
        self.food.penup()
        self.food.goto(randrange(-280, 281,20), randrange(-280, 281,20))
