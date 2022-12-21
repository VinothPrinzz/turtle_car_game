from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()

        self.shape('turtle')
        self.color('green')
        self.setheading(90)
        self.penup()
        self.goto(0, -280)

    def move(self):
        if self.ycor() < 280:
            self.forward(10)
