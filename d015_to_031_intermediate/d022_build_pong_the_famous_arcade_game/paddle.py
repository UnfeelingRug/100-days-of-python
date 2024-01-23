from turtle import Turtle


# Create the paddle, extending it lengthwise and facing it in the correct direction.
class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape('square')
        self.penup()
        self.speed('fastest')
        self.color('white')
        self.turtlesize(stretch_len=5, stretch_wid=1)
        self.setheading(90)
        self.goto(pos)

    # Go up and down when receiving input.
    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)
