from turtle import Turtle


# Create the ball, initializing its speed and direction.
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.move_speed = 0.1
        self.xdir = 1
        self.ydir = 1

    # Move the ball, setting new coordinates based on its current ones.
    def move(self):
        new_x = self.xcor() + (self.xdir * 10)
        new_y = self.ycor() + (self.ydir * 10)
        self.goto(new_x, new_y)

    # Bouncing the ball, reversing its X or Y direction based on what it hit.
    def bounce(self, hit):
        if hit == 'wall':
            self.ydir *= -1
        elif hit == 'paddle':
            self.move_speed *= 0.9
            self.xdir *= -1
        elif hit == 'reset':
            self.move_speed = 0.1
            self.xdir *= -1

    # Reset the ball's position to zero, its speed to the default value, and reverse its direction.
    def reset(self):
        self.goto(0, 0)
        self.bounce(hit='reset')
