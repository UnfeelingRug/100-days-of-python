# Importing the libraries needed for the game.
import os, random
from Higher_Lower_Game_Art import logo, vs
from Higher_Lower_Game_Data import data

# Select a rival for the provided account. Ensure it's not the same person, and that they don't have the same follower count.
def pick_rival(person):
    rival = random.choice(data)
    while rival == person or rival['follower_count'] == person['follower_count']:
        rival = random.choice(data)
    return rival

# Provide the person and return the formatted string with all of their info, grammatically correct.
def info_text(person):
    if person['description'][0] in ['a', 'e', 'i', 'o', 'u']:
        return(f'{person["name"]}, an {person["description"]} from {person["country"]}')
    else:
        return(f'{person["name"]}, a {person["description"]} from {person["country"]}')

# The bulk of the game itself.
def guessing_game(p1, p2, start=False):
    # Clear the screen and print the logo and the premise of the game.
    os.system('cls||clear')
    if start:
        print(f'{logo}Guess the account with more Instagram followers!')
    else:
        print(f'{logo}That\'s correct! Next up:')

    # Print the players up against each other with the VS logo in between.
    print(f'A. {info_text(p1)}{vs}B. {info_text(p2)}')

    # Get the player's input, ensure it's A or B. If not, prompt again.
    while True:
        guess = input('Who do you think has more followers, A or B? ').upper()
        if guess == 'A' or guess == 'B':
            break
    
    # If they guess right, loop through the game again, making B take A's spot and finding them a new rival. Otherwise, break the recursion loop.
    if guess == 'A' and p1['follower_count'] > p2['follower_count']:
        print('Correct!')
        return guessing_game(p2, pick_rival(p2)) + 1
    elif guess == 'B' and p2['follower_count'] > p1['follower_count']:
        print('Correct!')
        return guessing_game(p2, pick_rival(p2)) + 1
    else:
        return 0
    
# Pick the first person, find them a rival, and run the game to find the score.
starting_person = random.choice(data)
score = guessing_game(starting_person, pick_rival(starting_person), True)

# When the player loses, clear the screen and report their final score.
os.system('cls||clear')
print(f'{logo}Sorry, that\'s incorrect. Final Score: {score}')