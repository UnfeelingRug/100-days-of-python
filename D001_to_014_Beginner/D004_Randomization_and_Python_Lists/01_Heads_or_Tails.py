# This program will simply "flip a coin" and tell the user if they got heads or tails.
import random

# Generate a random integer between zero and one. If the result is 1, they got Heads. If the result is 0, they got Tails.
if random.randint(0, 1) == 1:
    print('Heads')
else:
    print('Tails')