from random import randint
from turtle import Turtle, Screen


# Generates a random color and returns it as a tuple.
def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


# Walk forward by 100, then turn to the right by the appropriate amount based on the number of sides.
# Note: For each shape, the angle should be 360° divided by the number of sides.
def draw_shape(sides):
    for i in range(sides):
        franklin.forward(100)
        franklin.right(360 / sides)


# Create the screen and set it to the correct colormode.
screen = Screen()
screen.colormode(255)

# Create Franklin the Turtle.
franklin = Turtle()
franklin.shape('turtle')

# Loop through this function from 3-10, deciding the number of sides.
for s in range(3, 11):
    franklin.color(random_color())
    draw_shape(s)

# Once everything is done, make the screen exit on click.
screen.exitonclick()
