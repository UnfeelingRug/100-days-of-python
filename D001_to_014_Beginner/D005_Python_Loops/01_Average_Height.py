# Input a list of student heights. Uncomment the second line to make it manual input.
# Input should be one string of numbers separated by only spaces. The program will split it into a list of individual items.
# student_heights = '180 124 165 173 189 169 146'.split()
student_heights = input('Give a list of heights in cm, separated only by spaces: ').split()

# Convert all of the heights in the list from strings to integers.
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

# Initialize variables for keeping track of certain items.
total = 0
number = 0

# Loop through the list, counting how many entries there are and adding them to the total.
for i in student_heights:
    total += i
    number += 1

# Divide the total by the number of entries and round to the nearest whole number.
average = round(total / number)

# And voila, we have our stats! Show them to the user.
print(f'Total Height: {total}')
print(f'Number of Students: {number}')
print(f'Average Height: {average}')