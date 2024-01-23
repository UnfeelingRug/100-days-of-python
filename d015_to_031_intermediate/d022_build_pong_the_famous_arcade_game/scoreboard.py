from turtle import Turtle
ALIGN = 'center'
FONT = ('Courier', 40, 'normal')


class Scoreboard(Turtle):
    # Creation; set the scoreboard at the top center with white coloration.
    def __init__(self):
        super().__init__()
        self.up()
        self.hideturtle()
        self.color('white')
        self.lscore = 0
        self.rscore = 0
        self.setpos(0, 240)
        self.update_score('init')

    # Updating score; increase the appropriate user's score variable by one and update the displayed text.
    def update_score(self, point):
        self.clear()
        if point == 'L':
            self.lscore += 1
        elif point == 'R':
            self.rscore += 1
        self.write(f'{self.lscore} - {self.rscore}', align=ALIGN, font=FONT)

    # When the game ends, report on the winner.
    def game_over(self):
        self.setpos(0, 0)
        if self.lscore > self.rscore:
            winner = 'Left'
        elif self.rscore > self.lscore:
            winner = 'Right'
        else:
            winner = 'No one'
        self.write(f'{winner} wins!', align=ALIGN, font=FONT)