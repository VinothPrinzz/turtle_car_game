from turtle import Turtle
import random


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.colors = ["red", "orange", "yellow", "green", "blue", "purple"]
        self.position = [(300, -250), (300, -220), (300, -190), (300, -160),
                         (300, -130), (300, -100), (300, -70), (300, -40), (300, -10), (300, 20)]
        self.segments = []
        self.movement = 5
        self.hideturtle()

    def create_car(self):
        random_change = random.randint(1, 6)
        if random_change == 6:
            tim = Turtle()
            tim.speed('slow')
            tim.penup()
            tim.shape('square')
            tim.shapesize(1, 2)
            tim.color(random.choice(self.colors))

            y = random.randint(-250, 250)
            tim.goto(300, y)
            tim.setheading(180)
            self.segments.append(tim)

    def move_car(self):
        for car in self.segments:
            car.forward(self.movement)

    def increase_speed(self):
        self.movement += 5
        self.move_car()
