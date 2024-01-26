from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    # Set appearance, set up in starting position and heading.
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.reset()

    # Move forward when receiving input from the player.
    def move(self):
        self.forward(MOVE_DISTANCE)

    # Check if the Turtle has reached the defined finish line.
    def check_pos(self):
        if self.ycor() > FINISH_LINE_Y:
            return True

    # Reset to the starting position.
    def reset(self):
        self.goto(STARTING_POSITION)