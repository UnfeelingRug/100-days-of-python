from turtle import Turtle
MOVE_DISTANCE = 20
EAST = 0
NORTH = 90
WEST = 180
SOUTH = 270


class Snake:
    def __init__(self):
        self.segments = []
        self.head = None
        self.create_snake()

    def create_snake(self):
        # Create the starting snake with three segments. Place it in the middle of the screen.
        self.segments = []
        for i in range(3):
            pos = (-20 * i), 0
            self.add_segment(pos)
        self.head = self.segments[0]

    # Move the snake by setting each back segment to the position of the one in front of it.
    # Once all the body pieces have been moved, make the head advance by one step in the current direction.
    def move(self):
        for i in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[i-1].xcor()
            new_y = self.segments[i-1].ycor()
            self.segments[i].setpos(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # Create a new segment of the snake at the given position.
    def add_segment(self, position):
        segment = Turtle('square')
        segment.color('white')
        segment.up()
        segment.setpos(position)
        self.segments.append(segment)

    # Extend the snake, to be used when eating food.
    def extend(self):
        self.add_segment(self.segments[-1].position())

    # Clear out all old snake segments, moving them off-screen, and create a new snake.
    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
            segment.hideturtle()
        self.segments.clear()
        self.create_snake()

    # The following four functions are meant to control the direction the snake's head faces.
    # It will not allow the snake to go 180° backwards. It can only go forward, right, or left.
    def up(self):
        if self.head.heading() != SOUTH:
            self.head.setheading(NORTH)

    def down(self):
        if self.head.heading() != NORTH:
            self.head.setheading(SOUTH)

    def left(self):
        if self.head.heading() != EAST:
            self.head.setheading(WEST)

    def right(self):
        if self.head.heading() != WEST:
            self.head.setheading(EAST)
