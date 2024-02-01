# I was given this code and asked to catch the exception given when the user asks for something outside of the possible range.
# I added an exception handler for IndexError, assigning a generic value to Fruit, and printed the pie in Finally after fixing the values.
fruits = ["Apple", "Pear", "Orange"]


def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        fruit = 'Fruit'
    finally:
        print(fruit + " pie")


make_pie(5)
