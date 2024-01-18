# Which year do you want to check?
year = int(input())

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")

# This code was given to me with out the input being wrapped in an int() function.
#   This would leave the input as a string, without allowing it to be used in the mathematical formulas ahead.