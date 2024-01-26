from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    # Define lists for cars and reserves, and set the stage to zero.
    def __init__(self):
        self.cars = []
        self.reserves = []
        self.stage = 0

    # Pull a car from the previous rounds' reserves, or create a new one if none are left.
    def add_car(self):
        if len(self.reserves) != 0:
            reserve_car = randint(0, len(self.reserves) - 1)
            self.cars.append(self.reserves[reserve_car])
            self.cars[-1].showturtle()
            del self.reserves[reserve_car]
        else:
            car = Turtle('square')
            car.color(choice(COLORS))
            car.penup()
            car.setheading(180)
            car.turtlesize(stretch_len=2, stretch_wid=1)
            car.setpos(300, randint(-250, 250))
            self.cars.append(car)

    # Move all cars forward by the appropriate distance.
    def move_cars(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE + (MOVE_INCREMENT * self.stage))

    # Increase the stage by one, resetting all cars' positions and colors and keeping them in reserves.
    def increase_stage(self):
        for car in self.cars:
            car.setpos(300, randint(-250, 250))
            car.hideturtle()
            car.color(choice(COLORS))
            self.reserves.append(car)
        self.cars = []
        self.stage += 1
