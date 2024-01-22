import os
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create the menu, coffee maker, and money machine from the existing classes.
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


while True:
    # Clear the old screen and begin again every loop.
    os.system('cls||clear')
    print('Welcome to the coffee machine!')

    # Take the user's input and store it as raw text. 
    # Fetches and displays options dynamically, in case new menu items are added.
    options = menu.get_items()
    order = input(f'What would you like to order? {options} ')

    # If the user orders 'off' exit the program. If they enter 'report' then run both the coffee maker and the money machine's Report methods.
    if order == 'off':
        print('\nThank you for using the coffee machine!')
        exit()
    elif order == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        # Check, in order, if the input is: A. On the menu.
        drink = menu.find_drink(order)
        if drink != None:
            # B. Possible to make, given the needed ingredients and the current resources, and C. Affordable by the user given their supplied coins.
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                # If all of these conditions are met, make the drink.
                coffee_maker.make_coffee(drink)
    # Hold up the loop until the user presses enter, allowing them to see the output before clearing and restarting the loop.
    input('Press enter to continue.')