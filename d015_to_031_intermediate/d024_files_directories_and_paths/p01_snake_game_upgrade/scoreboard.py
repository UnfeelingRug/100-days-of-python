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
        with open("high_score.txt") as high_score_archive:
            self.high_score = int(high_score_archive.read())
        self.setpos(0, 260)
        self.update_score()

    # Updating score; increase the score variable by one and update the displayed text.
    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f'Score: {self.score} | High Score: {self.high_score}', align=ALIGN, font=FONT)

    # When resetting the game, save the high score to the archive and update the HUD to match.
    def reset(self):
        if self.score > self.high_score:
            with open("high_score.txt", mode='w') as high_score_archive:
                high_score_archive.write(str(self.score))
            self.high_score = self.score
        self.score = 0
        self.clear()
        self.write(f'Score: {self.score} | High Score: {self.high_score}', align=ALIGN, font=FONT)

    # When the game ends, write that on the center of the screen.
    # This is currently commented out in favour of resetting the game to run again.
    # def game_over(self):
        # self.setpos(0, 0)
        # self.write('Game over!', align=ALIGN, font=FONT)
