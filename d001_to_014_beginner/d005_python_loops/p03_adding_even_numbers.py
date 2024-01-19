# This program will take a given number, and output the sum of every even number between 0 and it.
# If the user enters an incorrect number or even just text, they will be re-prompted.
while True:
    try:
        target = int(input('Please enter a number between 0 and 1000: '))
        if target >= 0 and target <= 1000:
            break
        else:
            print('Incorrect input. ', end='')
    except ValueError:
        print('Come on man, that wasn\'t even a number. ', end='')

sum = 0

# Count up from zero by twos until reaching the given number. Sum up the total.
for i in range(0, target+1, 2):
    sum += i

print(sum)