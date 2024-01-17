# This program calculates and returns the user's BMI by dividing their weight by their height squared.
height = float(input('How tall are you, in meters? '))
weight = int(input('How much do you weigh, in kilograms? Round to the nearest whole number. '))

BMI = int(float(weight) / (float(height) ** 2))
print(BMI)