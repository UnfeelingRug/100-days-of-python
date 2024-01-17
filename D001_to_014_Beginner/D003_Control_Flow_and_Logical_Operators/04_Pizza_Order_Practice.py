# This program will calculate the total cost of the user's order given their choices in the three questions.
print("Thank you for choosing Python Pizza Deliveries!")
size = input('What size of Pizza do you want? (S / M / L) ')
add_pepperoni = input('Would you like Pepperoni? (Y / N) ')
extra_cheese = input('Would you like Extra Cheese? (Y / N) ')

total = 0

if size == 'S':
    total += 15
    if add_pepperoni == 'Y':
        total += 2
elif size == 'M':
    total += 20
    if add_pepperoni == 'Y':
        total += 3
elif size == 'L':
    total += 25
    if add_pepperoni == 'Y':
        total += 3

if extra_cheese == 'Y':
    total += 1

print(f'Your final bill is: ${total}.')