# My solution to the following problem on reeborg.ca:
#   Maze

# Turn right by turning left three times.
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Until he reaches the exit, follow the usual rules of a maze.
# Turn right if possible, go straight if not, and turn left as a last resort.
while True:
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
    if at_goal():
        break