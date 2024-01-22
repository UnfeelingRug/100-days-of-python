from random import choice
from turtle import Turtle, Screen

# Colors, supplied by the colorgram-based extractor program we wrote and the supplied image.jpg file.
colors = [
    (252, 250, 247), (253, 247, 249), (237, 251, 245), (249, 228, 17),
    (213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20),
    (33, 90, 188), (43, 212, 71), (234, 148, 40), (33, 30, 152),
    (16, 22, 55), (66, 9, 49), (240, 245, 251), (244, 39, 149),
    (65, 202, 229), (14, 205, 222), (63, 21, 10), (224, 19, 111),
    (229, 165, 8), (15, 154, 22), (245, 58, 16), (98, 75, 9),
    (248, 11, 9), (222, 140, 203), (68, 240, 161), (10, 97, 62),
    (5, 38, 33), (68, 219, 155)
]


# Create a grid of dots X*Y, with the given size of dots and spacing.
def draw_hirst_image(x, y, dot_gap, dot_size):
    franklin.hideturtle()
    franklin.up()
    for drawY in range(y):
        for drawX in range(x):
            pick = choice(colors)
            franklin.color(pick)
            franklin.setpos(drawX*dot_gap, drawY*dot_gap)
            franklin.dot(dot_size)


# Create the screen and set it to the correct colormode.
screen = Screen()
screen.colormode(255)

# Create Franklin the Turtle and make him move at ludicrous speeds.
franklin = Turtle()
franklin.shape('turtle')
franklin.speed('fastest')

# Draw the Hirst-styled image by calling the function.
draw_hirst_image(10, 10, 50, 20)

# Once everything is done, make the screen exit on click.
screen.exitonclick()
