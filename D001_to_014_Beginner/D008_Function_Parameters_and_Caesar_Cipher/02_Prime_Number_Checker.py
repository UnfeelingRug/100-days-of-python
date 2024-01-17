# Creating a simple function to determine if a given number is a prime number.
# We'll do this by looping through every number from 2 to X-1, and seeing if the number is cleanly divisible.
# If it encounters no cases where it is divisible before reaching the end of the loop, it's a prime number.
def prime_checker(number):
    prime = True
    for i in range(2, number):
        if number % i == 0:
            prime = False
    if prime:
        print('This is a prime number.')
    else:
        print('This is not a prime number.')

n = int(input()) # Check this number
prime_checker(number=n)