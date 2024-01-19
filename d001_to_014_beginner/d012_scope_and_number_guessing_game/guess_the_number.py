import os, random
from art import logo

# Making the entire game a function to make it loopable.
def play():
    os.system('cls||clear')
    print(logo)
    print('Welcome to the number guessing game!')
    print('I\'m thinking of a number between 1 and 100...')
    secret_number = random.randint(1, 100)
    # print(f'DEBUG: Number is {secret_number}')

    # Prompt the user for a difficulty and set the number of guesses by that selection.
    while True:
        difficulty = input('Choose a difficulty. Type "Easy" or "Hard" to select: ').upper()
        if difficulty == 'EASY' or difficulty == 'E':
            guesses = 15
            break
        elif difficulty == 'HARD' or difficulty == 'H':
            guesses = 7
            break

    # Until they run out of guesses, tell the player whether they've guessed too high or too low, so they can hone in their guess.
    while guesses > 0:
        guess = int(input(f'\nMake a guess! (Remaining: {guesses}) '))
        guesses -= 1
        if guess == secret_number:
            print(f'You got it! The secret number was {secret_number}! ', end='')
            break
        elif guess < secret_number:
            print('Too low!')
        elif guess > secret_number:
            print('Too high!')

    # If the user runs out of guesses without guessing the correct number, console them.
    else:
        print(f'Sorry, you\'ve run out of guesses! The secret number was {secret_number}! ', end='')
    if input('Play again? [Y/N] ').upper() == 'Y':
        play()
    else:
        os.system('cls||clear')
        print('Thanks for playing...')
        print(logo)
        exit()

# Run the game.
play()