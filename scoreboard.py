from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1

    def levels(self):
        self.penup()
        self.clear()
        self.goto(0, 250)
        self.write(f'level: {self.level}', align='center',
                   font=('Courier', 24, 'normal'))
        self.hideturtle()

    def increase_levels(self):
        self.level += 1
        self.levels()
