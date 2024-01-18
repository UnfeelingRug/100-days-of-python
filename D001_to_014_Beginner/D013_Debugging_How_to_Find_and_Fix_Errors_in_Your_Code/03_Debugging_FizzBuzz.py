target = int(input())
for number in range(1, target + 1):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

# This code was given to me with multiple bugs and errors.
#   The FizzBuzz if statement was checking if the number was divisible by 3 OR 5, not both.
#   The elif statements were both ifs, meaning any number that met the criteria of 3 and/or 5 would print multiple times for one number.
#   This also broke the else statement, meaning every number not divisible by 5 would also print the number.
#   Finally, the number in print was surrounded in square brackets, meaning it would print a list containing the number rather than the number itself.