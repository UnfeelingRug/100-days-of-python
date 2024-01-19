# This is a rock-paper-scissors game against the computer. Try your best to win!

# First we'll make some ASCII art for the three outputs, plus a new-line separator for style.
from art import rock, paper, scissors, newline

import random
# Define the three possible moves in an indexible list.
moves = [rock, paper, scissors]

# Let the player choose their move from 0 to 2, and the computer will choose theirs from the same range.
# If the player tries to choose anything outside of the proper range, keep asking until they cooperate.
while True:
    player_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. '))
    if player_choice >= 0 and player_choice <= 2:
        break
python_choice = random.randint(0, 2)

# Once the player and PC have chosen, give a graphical representation of their choices.
print('The players have chosen; FIGHT!')
print(f'PLAYER CHOICE:\n{moves[player_choice]}{newline}PYTHON CHOICE:\n{moves[python_choice]}')

# If the player chooses the same move as the computer, they will tie.
if player_choice == python_choice:
    print('It\'s a draw!')
# If the player picks the move directly above the computer's, they will win.
# This also has a workaround for the looping of rock beating scissors despite their entries bring 0 and 2, respectively.
elif player_choice == python_choice + 1 or player_choice == python_choice - 2:
    print('You win!')
# In any other situation, the player will lose.
else:
    print('You lose!')