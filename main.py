from turtle import Screen
from player import Player
from car import Car
from time import sleep
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

player = Player()
cars = Car()


screen.listen()
screen.onkey(player.move, 'Up')

score = ScoreBoard()
score.levels()

game_on = True
while game_on:
    sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_car()
    for car in cars.segments:
        if player.distance(car) < 25:
            game_on = False
            player.write('Game Over', align='center', font=('Arial', 24, 'normal'))

    if player.ycor() == 280:
        player.goto(0, -280)
        score.levels()
        score.increase_levels()
        cars.increase_speed()


screen.exitonclick()
