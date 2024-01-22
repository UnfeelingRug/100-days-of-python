from turtle import Turtle
ALIGN = 'center'
FONT = ('Courier', 15, 'normal')


class Scoreboard(Turtle):
    # Creation; set the scoreboard at the top center with white coloration.
    def __init__(self):
        super().__init__()
        self.up()
        self.hideturtle()
        self.color('white')
        self.score = -1
        self.setpos(0, 260)
        self.update_score()

    # Updating score; increase the score variable by one and update the displayed text.
    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f'Score: {self.score}', align=ALIGN, font=FONT)

    def game_over(self):
        self.setpos(0, 0)
        self.write('Game over!', align=ALIGN, font=FONT)