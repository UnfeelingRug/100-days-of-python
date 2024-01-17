# My solution to the following problem on reeborg.ca:
#   Around 1 - Apple

# Step away from home to begin.
move()

# If overtop of an apple, pick it up. Then check if you should walk forward or turn left, and do so until you reach home.
while not at_goal():
    if object_here('apple'):
        take()
    if front_is_clear():
        move()
    else:
        turn_left()