# A very simple calculator app that takes user input and performs the requested operations.
import os
from art import logo

# Define the four functions to do the different mathematical operators.
def add(n1, n2):
    '''Increases the first input by the value of the second.'''
    return n1 + n2

def subtract(n1, n2):
    '''Reduces the first input by the value of the second.'''
    return n1 - n2

def multiply(n1, n2):
    '''Multiplies the first input by the value of the second.'''
    return n1 * n2

def divide(n1, n2):
    '''Divides the first input by the value of the second.'''
    return n1 / n2

def exponent(n1, n2):
    return n1 ** n2

def calculator():
    os.system('cls||clear')
    print(logo)
    num1 = float(input('What is the first number? '))

    while True:
        for i in operations:
            print(f'[{i}]', end=' ')
        while True:
            operation = input('←←← Pick an operation from the list: ')
            if operation not in operations:
                print('Not a valid choice! ', end='')
            else:
                break
        num2 = float(input('What is the second number? '))

        answer = operations[operation](num1, num2)
        print(f'{num1} {operation} {num2} is {answer}')

        continue_state = input(f'Type "Y" to continue calculating with {answer}, "N" to start a new calculation from scratch, or anything else to exit: ').upper()

        if continue_state == 'Y':
            num1 = answer
        elif continue_state == 'N':
            calculator()
        else:
            print('Thanks for using my calculator!')
            exit()

# Define a dictionary that lists the operations with their respective symbols as keys.
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '**': exponent,
}

calculator()