# Anything from input comes in as a string automatically, but we can do all kinds of things with that.
# In this example, we simply took each individual digit, turned them into ints, and added them together.
two_digit_number = input('Please give me a two-digit number: ')
print(int(two_digit_number[0]) + int(two_digit_number[1]))