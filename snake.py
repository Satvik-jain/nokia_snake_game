from turtle import Turtle, Screen

screen = Screen()
starting_position = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
class Snake:
    def __init__(self):
        self.segments = []
        self.create()

    def create(self):
        for position in starting_position:
            new = Turtle('square')
            new.color('white')
            new.penup()
            new.goto(position)
            self.segments.append(new)

        screen.update()

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(move_distance)
