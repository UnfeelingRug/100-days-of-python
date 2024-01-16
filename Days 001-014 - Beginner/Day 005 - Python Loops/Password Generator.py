#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Set defaults for the number of letters, numbers, and symbols to include in the password. Delete the numbers and uncomment the inputs to customize it at runtime.
print("Welcome to the PyPassword Generator!")
nr_letters = 8 #int(input("How many letters would you like in your password? "))
nr_symbols = 2 #int(input(f"How many symbols would you like? "))
nr_numbers = 5 #int(input(f"How many numbers would you like? "))

#Easy Level - Order is of characters is not randomised:
#e.g. 4 letter, 2 symbol, 2 number = AAAA!!11
password = random.choices(letters, k=nr_letters) + random.choices(symbols, k=nr_symbols) + random.choices(numbers, k=nr_numbers)
print('Easy-Level Password: ', end='')
for i in password:
    print(i, end='')
print()

#Hard Level - Order of characters is randomised:
#e.g. 4 letter, 2 symbol, 2 number = A1!AA!1A
# Achieve this by simply running the random.shuffle() function on the password generated in the Easy mode.
random.shuffle(password)
print(f'Hard-Level Password: ', end='')
for i in password:
    print(i, end='')
print()