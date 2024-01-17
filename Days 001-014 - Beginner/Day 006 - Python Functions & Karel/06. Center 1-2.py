# My solution to the following problems on reeborg.ca:
#   Center 1
#   Center 2

# Turn around the number of times specified in the function call.
def turn_around(x):
    for i in range(x):
        turn_left()

# Walk to the end, counting half the number of steps.
# After reaching the end, turn around and walk that many steps back, and you will be in the middle.
def find_middle():
    length = 0.5
    while True:
        if front_is_clear():
            move()
            length += 0.5
        else:
            length = int(length)
            turn_around(2)
            for i in range (length):
                move()
            break

# Find the horizontal middle, turn to face north, and then find the vertical middle.
# Once found, place a Token in the center of the map.
find_middle()
turn_around(3)
find_middle()
put()