from turtle import Turtle, Screen

screen = Screen()
starting_position = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create()
        self.head = self.segments[0]
    def create(self):
        for position in starting_position:
            new = Turtle('square')
            new.color('green')
            new.penup()
            new.goto(position)
            self.segments.append(new)

    def add(self):
        new = Turtle('square')
        new.color('green')
        new.penup()
        new.hideturtle()
        self.segments.append(new)

        screen.update()

    def move(self):
        self.segments[-1].showturtle()
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(move_distance)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def check_wall(self):
        if self.segments[0].xcor() >= 300 or self.segments[0].xcor() <= -290 or \
                self.segments[0].ycor() >= 300 or self.segments[0].ycor() <= -290:
            return False
        else:
            return True
