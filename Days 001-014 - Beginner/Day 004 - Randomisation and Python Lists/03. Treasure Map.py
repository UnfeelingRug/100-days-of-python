# This program will create a treasure map, hiding the treasure in the plot chosen by the user.

# Begin by initializing the map. Define three lists, or three Rows, then stick them together into another list to make Columns.
# Remember that a list of lists is, for all intents and purposes, a table, where each smaller list is a row in the larger list.
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]

# Prompt the user to pick a plot to bury their treasure in, from A1 to C3.
print("Prepare to hide your treasure! Remember, X marks the spot.")
position = input('Where would you like to bury the treasure? (A-C, 1-3) ')

try:
    # Define the column by checking the letter portion of the input against a given list.
    # Define the row by subtracting one from the given number portion of the input.
    column = ['A', 'B', 'C'].index(position[0].upper())
    row = int(position[1]) - 1

    # Take the calculated row and column, and replace that element with a big red X to mark the spot.
    map[row][column] = '❌'

    print(f"{line1}\n{line2}\n{line3}")
except:
    # If the user provides invalid input (anything not A1-C3), they will be booted out.
    print('You did not supply a valid input despite clear instructions. No treasure for you!')