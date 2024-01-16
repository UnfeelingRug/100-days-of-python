# Input a list of student scores, separated by only spaces.
# The program will split them into individual entries and turn them into integers.
# student_scores = '78 65 89 86 55 91 64 89'.split()
student_scores = input('Give a list of scores, separated by only spaces: ').split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

# Initialize the maximum at 0 and loop through the list.
# If a score is higher than the current max, make it the new max. Otherwise, move on.
max = 0
for i in student_scores:
    if i > max:
        max = i

print(f'The highest score in the class is: {max}')