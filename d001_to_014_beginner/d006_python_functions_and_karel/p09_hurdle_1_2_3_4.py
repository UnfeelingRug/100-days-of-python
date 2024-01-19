# My solution to the following problems on reeborg.ca:
#   Hurdle 1
#   Hurdle 2
#   Hurdle 3
#   Hurdle 4

# Turning right is not allowed by default. Three left turns will get us there.
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# To jump a hurdle, we want to turn left to face upwards, go up until there is no longer a space to the right of us, turn right, move, then right again to face downwards.
# After that, we want to continue down until there is no more space below, then turn left to prepare for the next instruction.
def hurdle():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

# If we aren't at the goal yet, walk until there's something in front of you. When there is, begin the hurdle function.
while not at_goal():
    if wall_in_front():
        hurdle()
    else:
        move()