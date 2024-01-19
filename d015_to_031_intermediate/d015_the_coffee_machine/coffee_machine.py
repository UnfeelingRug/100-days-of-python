import os
from menu import MENU, resources

def report():
    '''Prints a report of how many resources are in the system.'''
    print('Water:', resources['water'])
    print('Milk:', resources['milk'])
    print('Coffee:', resources['coffee'])
    print(f'Money: ${resources["money"]:0.2f}\n')

def off():
    '''Disables the system, thanking the user before closing the program.'''
    os.system('cls||clear')
    print('Thank you for using the coffee machine!')
    exit()

def order():
    '''Ask the user for their order until they provide a valid input; either a coffee order or a hidden command like Report or Off.'''
    while True:
        order = input('What would you like? [Espresso, Latte, Cappuccino] ').lower()
        if order in ['espresso', 'latte', 'cappuccino']:
            return order
        elif order in commands:
            commands[order]()

def check_drink(drink):
    '''Check if the given drink is possible to make, given the required ingredients and available resources.'''
    in_stock = True
    for i in drink['ingredients']:
        if resources[i] < drink['ingredients'][i]:
            print(f'Sorry, there is not enough {i}!')
            in_stock = False
    print()
    return in_stock

def take_money(cost):
    '''Prompt the user for the number of coins to put in the machine, and provide an appropriate response based on the payment amount versus cost of the drink.'''
    pay = int(input('How many quarters? ')) * 0.25
    pay += int(input('How many dimes? ')) * 0.1
    pay += int(input('How many nickels? ')) * 0.05
    pay += int(input('How many pennies? ')) * 0.01
    print()
    if pay > cost:
        resources['money'] += cost
        print(f'Thank you for your payment! Here is ${pay - cost:0.02f} in change and ', end='')
        return True
    elif pay == cost:
        resources['money'] += cost
        print(f'Thank you for your payment! Here is ', end='')
        return True
    elif pay < cost:
        print('Not enough money - sorry, we aren\'t a charity!')
        return False

# Initializing the list of extra commands and their corresponding functions.
commands = {
    'off': off,
    'report': report,
}

# Loop through the program, prompting the user for new orders and pausing the loop at the end so the user can read the output before clearing the screen and continuing.
while True:
    os.system('cls||clear')
    print('Welcome to the coffee machine!')
    drink = order()
    if check_drink(MENU[drink]):
        if take_money(MENU[drink]['cost']):
            print(f'your {drink} ☕ Enjoy!')
            for ingredient in MENU[drink]['ingredients']:
                resources[ingredient] -= MENU[drink]['ingredients'][ingredient]
    input('Press enter to continue.')