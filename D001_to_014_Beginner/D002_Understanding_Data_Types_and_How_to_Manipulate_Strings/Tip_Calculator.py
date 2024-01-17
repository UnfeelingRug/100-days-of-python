print('Welcome to the tip calculator!')
bill = float(input('How much was the total bill? $'))
tip = int(input('What percentage tip would you like to give? ')) / 100 + 1
people = int(input('How many people are splitting the bill? '))

# The split will automatically be formatted to two decimal places, even when it would be an even number like $56.00
total = bill * tip
split = "{:.2f}".format(total / people)

print(f'Each person should pay: ${split}')