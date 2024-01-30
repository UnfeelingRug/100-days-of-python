import pandas

# Generate a dictionary of the NATO Phonetic Alphabet based on the imported CSV file.
nato_alphabet = {row.letter: row.code for (index, row) in pandas.read_csv('nato_phonetic_alphabet.csv').iterrows()}

# Take a word from the user as input, then return it to them as NATO-ized as a list.
word = input('Enter a word: ').upper()
nato_word = [nato_alphabet[char] for char in word]
print(nato_word)
