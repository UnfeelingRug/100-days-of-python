# My solution to the following problems on reeborg.ca:
#   Around 1
#   Around 1 - Variable
#   Around 2
#   Around 3
#   Around 4

# Turn right by turning left three times.
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Put down one of the tokens Reeborg is carrying and follow the normal routine to step away from it.
# This loop will not check for the token, because we don't want to exit out early while he's still navigating away from it.
put()
while object_here('token'):
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

# Until he reaches the token again, walk forward unless he reaches a turn, defined by a wall in front (turn left) or an open space to the right (turn right).
# If he reaches either of those scenarios, turn left or right as appropriate and continue moving.
while True:
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
    if object_here('token'):
        break