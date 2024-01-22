from turtle import Turtle
MOVE_DISTANCE = 20
EAST = 0
NORTH = 90
WEST = 180
SOUTH = 270


class Snake:
    def __init__(self):
        # Create the starting snake with three segments. Place it in the middle of the screen.
        self.segments = []
        for i in range(3):
            segment = Turtle('square')
            segment.color('white')
            segment.up()
            segment.setpos(-20*i, 0)
            self.segments.append(segment)

    # Move the snake by setting each back segment to the position of the one in front of it.
    # Once all the body pieces have been moved, make the head advance by one step in the current direction.
    def move(self):
        for i in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[i-1].xcor()
            new_y = self.segments[i-1].ycor()
            self.segments[i].setpos(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    # The following four functions are meant to control the direction the snake's head faces.
    # It will not allow the snake to go 180° backwards. It can only go forward, right, or left.
    def up(self):
        if self.segments[0].heading() != SOUTH:
            self.segments[0].setheading(NORTH)

    def down(self):
        if self.segments[0].heading() != NORTH:
            self.segments[0].setheading(SOUTH)

    def left(self):
        if self.segments[0].heading() != EAST:
            self.segments[0].setheading(WEST)

    def right(self):
        if self.segments[0].heading() != WEST:
            self.segments[0].setheading(EAST)
