# Importing modules to get the random functions and the extra assets without clouding up this file.
import random
from hangman_art import logo
from hangman_art import stages
from hangman_words import word_list

# Pick a mystery word from the supplied list, and create the list for guessed letters.
mystery_word = random.choice(word_list).upper()
guessed_list = []
lives = len(stages) - 1

# Welcome the user to the game. If you want to test, uncomment the second line here.
print(logo, end='')
#print(f'Secret Word: {mystery_word}')

# Ask the user for input until they give an appropriate guess.
def prompt_guess():
    while True:
        guess = input('Guess a letter from A-Z: ').upper()
        if guess in guessed_list:
            print('You already guessed that one! ', end='')
        elif guess.isalpha() and len(guess) == 1:
            guessed_list.append(guess)
            return guess
        else:
            print('That\'s not a single letter! ', end='')

# Print the mystery word, replacing unguessed letters with blanks.
def print_word():
    print(stages[lives])
    for char in mystery_word:
        if char in guessed_list:
            print(char, end=' ')
        else:
            print('_', end=' ')
    print()

# Check if every letter in the mystery word has been guessed. If so, tell the player they've won.
def check_victory():
    for char in mystery_word:
        if char not in guessed_list:
            return False
    return True

# Loop through the different functions as needed, until victory or failure.
def game_loop():
    global lives
    while True:
        if not check_victory():
            print_word()
            if(prompt_guess()) in mystery_word:
                print('\nNice guess!')
            else:
                lives -= 1
                if lives == 0:
                    print_word()
                    print(f'Sorry, you lose! The man has been hanged. The word was: {mystery_word}')
                    break
                else:
                    print(f'\nToo bad! Lives remaining: {lives}')
        else:
            print_word()
            print('Congratulations, you win! The man lives to hang another day.')
            break

game_loop()