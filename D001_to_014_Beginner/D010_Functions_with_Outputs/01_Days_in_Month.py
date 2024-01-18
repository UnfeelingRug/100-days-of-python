# A program to tell us how many days are in any given month, in any given year.
def is_leap(year):
    '''Takes a given year as input, returning True or False based on whether or not it is a leap year.'''
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
  
# Get the number of days in each month as defined by the list, add one if it's a February in a leap year, then return the result.
def days_in_month(month, year):
    '''Take the given month and year, then return the number of days it has.'''
    month_days = {
        'January': 31,
        'February': 28,
        'March': 31,
        'April': 30,
        'May': 31,
        'June': 30,
        'July': 31,
        'August': 31,
        'September': 30,
        'October': 31,
        'November': 30,
        'December': 31
        }
    if month == 'February':
        if is_leap(year):
            return month_days[month] + 1
    return month_days[month]
  
# Get the user's input of year and month they want to check, then do the calculations and let them know.
year = int(input('Enter a year: ')) # Enter a year
month = input('Enter a month: ')
days = days_in_month(month, year)
print(f'{month} {year} has {days} days in it.')