from Caesar_Cipher_Art import logo

print(logo)

# A simple program to recreate the Caesar Cipher, by shifting letters by a certain amount down the alphabet.
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Encrypting by taking the base message, shifting it forward the given amount, and returning the encrypted message to the user.
def caesar(direction, input, shift):
    new_text = ''
    if direction == 'decode':
        shift *= -1
    for char in input:
        if char.isalpha():
            new_char = alphabet.index(char) + shift
            if new_char > 25:
                new_char -= 26
            elif new_char < 0:
                new_char += 26
            new_text += alphabet[new_char]
        else:
            new_text += char
    print(f'The {direction}d result is: {new_text}')

while True:
    # Get the user's input on whether they want to encrypt or decrypt, plus the message and the number of letters to shift.
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: ")) % 26

    caesar(direction, text, shift)
    replay = input('Would you like to run the program again? [Y/N] ').upper()
    if replay != 'Y':
        print('Okay, goodbye!')
        break