import pandas

# Generate a dictionary of the NATO Phonetic Alphabet based on the imported CSV file.
nato_alphabet = {row.letter: row.code for (index, row) in pandas.read_csv('nato_phonetic_alphabet.csv').iterrows()}

# Take a word from the user as input, then return it to them as NATO-ized as a list.
# If they enter something outside of the valid entries, warn them, and prompt them to retry.
while True:
    word = input('Enter a word: ').upper()
    try:
        output = [nato_alphabet[char] for char in word]
    except KeyError:
        print('Please enter a single word with only letters from A-Z.')
    else:
        print(output)
        break
