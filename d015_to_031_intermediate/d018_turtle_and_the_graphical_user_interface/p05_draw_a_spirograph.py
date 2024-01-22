from random import randint
from turtle import Turtle, Screen


# Generates a random color and returns it as a tuple.
def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


# Spin in a circle in increments of the given value, drawing circles of random colors each time.
def draw_spirograph(size_of_gap):
    for i in range(0, 360, size_of_gap):
        franklin.color(random_color())
        franklin.setheading(i)
        franklin.circle(100)


# Create the screen and set it to the correct colormode.
screen = Screen()
screen.colormode(255)

# Create Franklin the Turtle and make him move at ludicrous speeds.
franklin = Turtle()
franklin.shape('turtle')
franklin.speed('fastest')

# Draw the spirograph by calling the function.
draw_spirograph(5)

# Once everything is done, make the screen exit on click.
screen.exitonclick()
