from random import randint
from turtle import Turtle


class Food(Turtle):
    # Creation; make the food display as small blue circles.
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed('fastest')
        self.refresh()

    # Refreshing location; picking a grid space and going there.
    def refresh(self):
        random_x = randint(-13, 13) * 20
        random_y = randint(-13, 13) * 20
        self.setpos(random_x, random_y)