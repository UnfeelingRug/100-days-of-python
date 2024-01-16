# This program will estimate how many weeks the user has left in their life, assuming they just reached their current and and they will live to be 90.
age = input('How old are you right now? ')

weeks = (90 - int(age)) * 52
print(f'You have {weeks} weeks left.')