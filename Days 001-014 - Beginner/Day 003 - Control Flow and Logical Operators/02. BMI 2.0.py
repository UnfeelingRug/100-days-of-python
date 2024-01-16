# This is a more refined version of the older BMI calculator that will also tell you your BMI category (eg. underweight, obese, etc)
height = float(input('How tall are you, in meters? '))
weight = int(input('How much do you weigh, in kilograms? Round to the nearest whole number. '))

BMI = weight / height ** 2

if BMI < 18.5:
    print(f'Your BMI is {BMI}, you are underweight.')
elif BMI < 25:
    print(f'Your BMI is {BMI}, you have a normal weight.')
elif BMI < 30:
    print(f'Your BMI is {BMI}, you are slightly overweight.')
elif BMI < 35:
    print(f'Your BMI is {BMI}, you are obese.')
else:
    print(f'Your BMI is {BMI}, you are clinically obese.')