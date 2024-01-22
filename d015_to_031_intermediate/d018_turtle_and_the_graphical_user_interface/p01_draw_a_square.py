from turtle import Turtle, Screen

# Create Franklin the Turtle, make him pink.
franklin = Turtle()
franklin.shape('turtle')
franklin.color('#F88CAD')

# Make Franklin walk 100 paces, then turn to his right and do it again. Four times to draw a square.
for i in range(4):
    franklin.forward(100)
    franklin.right(90)

# Create the screen and make it exit on click.
screen = Screen()
screen.exitonclick()