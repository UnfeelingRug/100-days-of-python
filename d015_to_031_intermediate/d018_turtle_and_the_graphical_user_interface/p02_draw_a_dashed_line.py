from turtle import Turtle, Screen

# Create Franklin the Turtle, make him pink.
franklin = Turtle()
franklin.shape('turtle')
franklin.color('#F88CAD')

# Make Franklin walk 10 steps drawing, then 10 steps not drawing, fifteen times, to draw a dashed line.
for i in range(15):
    franklin.down()
    franklin.forward(10)
    franklin.up()
    franklin.forward(10)

# Create the screen and make it exit on click.
screen = Screen()
screen.exitonclick()