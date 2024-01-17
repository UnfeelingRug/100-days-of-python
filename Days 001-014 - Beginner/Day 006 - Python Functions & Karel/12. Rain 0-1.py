# My solution to the following problems on reeborg.ca:
#   Rain 0
#   Rain 1

# Turn left three times to turn right.
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Hardcoded setup for the loop.
move()
turn_right()
move()

# If Reebot is at the goal, he should stop everything. If there's a gap to his right, build a wall and face the path again.
# If there's no gap, either go straight, or turn left if going straight is obstructed.
while True:
    if at_goal():
        break
    elif right_is_clear():
        turn_right()
        build_wall()
        turn_left()
    elif wall_in_front():
        turn_left()
    elif front_is_clear():
        move()