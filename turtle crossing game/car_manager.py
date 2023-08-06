from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.cars = []
        self.currentSpeed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            x = 280
            y = random.randint(-250, 250)
            new_car = Turtle("square")
            new_car.pu()
            new_car.shapesize(1, 3)
            new_car.goto(x, y)
            random_color = random.choice(COLORS)
            new_car.color(random_color)
            self.cars.append(new_car)


    def move_cars(self):
        for car in self.cars:
            car.backward(self.currentSpeed)

    def increase_speed(self):
        self.currentSpeed = self.currentSpeed + MOVE_INCREMENT
        self.move_cars()
