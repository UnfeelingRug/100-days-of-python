# This is FizzBuzz!
# Your program should print every number from 1 to 100, including 100.
# If the number is divisible by three, it should instead print "Fizz"
# If the number is divisible by five, it should instead print "Buzz"
# If the number is divisible by BOTH, it should print "FizzBuzz"

# Check if it's divisible by both, then just by 3, then just by 5, otherwise print normally.
for i in range (1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)