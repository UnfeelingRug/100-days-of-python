print('Welcome to the tip calculator!')
bill = float(input('How much was the total bill? $'))
tip = int(input('What percentage tip would you like to give? ')) / 100 + 1
people = int(input('How many people are splitting the bill? '))

total = bill * tip
split = "{:.2f}".format(round(total / people, 2))

print(f'Each person should pay: ${split}')