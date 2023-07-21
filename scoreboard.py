from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.refresh()
        self.hideturtle()


    def gameover(self):
        self.home()
        self.write("GAME OVER", align="center", font=("Arial", 30, "normal"))

    def add_score(self):
        self.score += 1
    def refresh(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 16, "normal"))
