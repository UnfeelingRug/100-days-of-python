# This program will tell the user if the given year is a Leap Year.
year = int(input('What year do you want to check? '))

# If the year is cleanly divisible by 4, it's a Leap Year.
if year % 4 == 0:
    # Unless it's also cleanly divisible by 100, in which case it's NOT a Leap Year.
    if year % 100 == 0:
        # That is, unless it's ALSO cleanly divisible by 400, in which case it actually IS a Leap Year.
        if year % 400 == 0:
            print(f'{year} is a Leap Year!')
        else:
            print(f'{year} is not a Leap Year.')
    else:
        print(f'{year} is a Leap Year!')
else:
    print(f'{year} is not a Leap Year.')