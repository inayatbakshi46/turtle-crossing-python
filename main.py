import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
turtle = Player()
cars = CarManager()
score = Scoreboard()
screen.listen()
screen.onkey(turtle.up ,"Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move()
    for car in cars.all_cars:
        if car.distance(turtle) < 20:
            score.gameover()
            game_is_on = False
            
    if turtle.is_at_finish():
        score.level_up()
        turtle.goto_start()
        cars.level_up()


screen.exitonclick()