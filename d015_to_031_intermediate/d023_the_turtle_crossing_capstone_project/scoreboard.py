from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    # Set position and hide the Turtle.
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 0
        self.setpos(-280, 250)
        self.update_score()

    # Clear the previous writing, increase the score, and rewrite.
    def update_score(self):
        self.clear()
        self.level += 1
        self.write(f'Level: {self.level}', align='left', font=FONT)

    # Write the "Game Over!" message in the center of the screen.
    def game_over(self):
        self.setpos(0, 0)
        self.write('Game Over!', align='center', font=FONT)
