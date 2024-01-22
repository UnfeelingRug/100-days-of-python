from random import choice, randint
from turtle import Turtle, Screen


# Generates a random color and returns it as a tuple.
def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


# Create the screen and set it to the correct colormode.
screen = Screen()
screen.colormode(255)

# Create Franklin the Turtle, make his pen bigger and make him move at ludicrous speeds.
franklin = Turtle()
franklin.shape('turtle')
franklin.pensize(10)
franklin.speed('fastest')

# Walk 250 times in a random cardinal direction, picking a new color every time from random RGB values.
for i in range(250):
    franklin.color(random_color())
    franklin.setheading(choice([0, 90, 180, 270]))
    franklin.forward(30)

# Once everything is done, make the screen exit on click.
screen.exitonclick()
