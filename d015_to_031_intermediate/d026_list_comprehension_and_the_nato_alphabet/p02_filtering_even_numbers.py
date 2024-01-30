list_of_strings = '1, 1, 2, 3, 5, 8, 13, 21, 34, 55'.split(',')

# Turn the split strings into ints, then filter out every one that is not an even number.
list_of_numbers = [int(n) for n in list_of_strings]
result = [n for n in list_of_numbers if n % 2 == 0]
print(result)