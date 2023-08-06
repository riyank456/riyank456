import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player1 = Player()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(fun=player1.move, key="Up")
car_manager = CarManager()
score_board = Scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.cars:
        if player1.distance(car) < 20:
            score_board.game_over()
            game_is_on = False


    if player1.ycor() == 280:
        player1.goto(0,-280)
        score_board.update()
        car_manager.increase_speed()


screen.exitonclick()