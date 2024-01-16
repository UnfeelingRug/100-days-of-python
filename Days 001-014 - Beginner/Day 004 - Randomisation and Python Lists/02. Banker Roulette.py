# This program will take a given list of names and pick one from the list.
import random

# Pre-supplying names for ease of testing. Uncomment the second line to allow manual input.
names_string = 'Angela, Ben, Jenny, Michael, Chloe'
# names_string = input('List all of the people who ate together, each separated by a comma and a space: ')
names = names_string.split(", ")

# Pick a person from the list using a random number. Not using choice() because that was not allowed for this challenge.
loser = names[random.randint(0, len(names)-1)]
print(f'{loser} is going to buy the meal today!')

# If I DID want to use choice, it would make this much easier.
# loser = random.choice(names)
# print(f'{loser} is going to buy the meal today!')