# A simple program to categorize students' progress based on their current scores.
# First, establish the dictionary of students and their scores.
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

# Create a new dictionary to hold their grading categories.
student_grades = {}

# Copy the students from the student_scores dictionary to the student_grades dictionary, replacing their score numbers with the appropriate categories.
for student in student_scores:
    if student_scores[student] > 90:
        student_grades[student] = 'Outstanding'
    elif student_scores[student] > 80:
        student_grades[student] = 'Exceeds Expectations'
    elif student_scores[student] > 70:
        student_grades[student] = 'Acceptable'
    else:
        student_grades[student] = 'Fail'

# Print the list of students and their grades.
print(student_grades)