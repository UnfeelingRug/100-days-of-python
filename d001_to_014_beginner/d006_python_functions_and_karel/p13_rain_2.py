# My solution to the following problem on reeborg.ca:
#   Rain 2

# Turn left three times to turn right.
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
# If Reebord comes to a gap, he'll be unsure if he needs to build a wall or turn right. This should check for him.
# If he steps forward and there's still a wall, he should go back and fix the hole. Otherwise, he should go back and turn right.
def check_wall():
    move()
    if wall_on_right():
        turn_left()
        turn_left()
        move()
        turn_left()
        build_wall()
        turn_left()
    else:
        turn_left()
        turn_left()
        move()
        turn_left()
        move()

# Hardcoded setup for the loop.
move()
move()
move()
turn_right()
move()

# If Reebot is at the goal, he should stop everything. If there's a gap to his right, he'll check if it's a hole or a turn and act accordingly.
# If there's no gap, either go straight, or turn left if going straight is obstructed.
while True:
    if at_goal():
        break
    elif right_is_clear():
        check_wall()
    elif wall_in_front():
        turn_left()
    elif front_is_clear():
        move()