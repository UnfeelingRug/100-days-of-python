# Take the input sentence.
sentence = 'What is the Airspeed Velocity of an Unladen Swallow?'

# Break the sentence string into a list of words, make a dictionary with the words as keys and their lengths as values.
result = {word:len(word) for word in sentence.split()}
print(result)
