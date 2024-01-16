# You can reassign values to variables even after they've been assigned.
# In this example, we want to swap the values of a and b.
a = input('Give me a word! a: ')
b = input('And another one? b: ')

print('Great, now I\'ll swap their spots! Observe...')

# Uncomment these lines to swap using a more 'conventional' method. A bit clunky, but understandable.
temp = a
a = b
b = temp

# Uncomment this line to swap variables using tuples. Easy and quick.
# a, b = b, a

print("a is now: " + a)
print("b is now: " + b)