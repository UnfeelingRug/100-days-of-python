# A simple program to run a blind auction, clearing the screen between each bidder.
# Import OS package for the ability to clear the output terminal.
import os
from art import logo

# Defining the function for getting a new bidder; ask for their name and how much they'd like to bid.
# Add them to the bidders dictionary with their name as the key, and their bid as the value.
def new_bidder():
    name = input('What is your name? ')
    bid = int(input('What is your bid? $'))
    bidders[name] = bid

# Initializing the bidders dictionary.
bidders = {}

# Until the user responds that there are no more bidders, follow the loop.
# Clear the screen to erase old bids, print the logo, welcome the new user, and ask them for their name and bid.
# Once the last user responds that there are no more users, break out of the loop.
while True:
    os.system('cls||clear')
    print(logo)
    print('Welcome to the blind auction!')
    new_bidder()
    if input('Are there any other bidders? [Y/N] ').upper() != 'Y':
        break

# Set variables to track the winner and their bid, then loop through the dictionary to find the maximum value.
winner = ''
winning_bid = 0
for name in bidders:
    if bidders[name] > winning_bid:
        winner = name
        winning_bid = bidders[name]

# Clear the screen one last time, then report the winner and their bid.
os.system('cls||clear')
print(f'The winner is {winner}, with a bid of ${winning_bid}!')