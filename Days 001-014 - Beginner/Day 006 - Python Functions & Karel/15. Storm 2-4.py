# My solution to the following problems on reeborg.ca:
#   Storm 2
#   Storm 3
#   Storm 4 (Note: I was unable to figure out any optimizations. The creator got it down to 126, but the best I could figure out was 461. Oof.)

# Defining a variable to tell the program if Reeborg is finished or not.
finished = False

# Define the ability to turn any given number of times.
def turn_x(x):
    for i in range(x):
        turn_left()
        
# Check in place for leaves and gather as many as are there.
def check_leaves():
    while object_here('leaf'):
        take('leaf')

# If you discover an obstacle, go around it.
def go_around():
    check_leaves()
    turn_x(3)
    move()
    turn_left()
    move()
    move()
    turn_left()
    move()
    turn_x(3)

# Go forward until there is no longer a free space in front of you.
def sweep():
    while front_is_clear():
        check_leaves()
        move() 

# When returned to the bottom-right corner facing the end, walk home and deposit the leaves.
def go_home():
    while front_is_clear():
        move()
    turn_x(3)
    while carries_object('leaf'):
        toss('leaf')

# When reaching the end of a row, turn around and go back on the next row.
def snake():
    global finished
    check_leaves()
    if is_facing_north():
        turn_x(3)
        if wall_in_front():
            turn_x(3)
            while not wall_in_front():
                move()
            turn_x(3)
            go_home()
            finished = True
            return
        move()
        turn_x(3)
    else:
        turn_left()
        if wall_in_front():
            turn_x(2)
            go_home()
            finished = True
            return
        move()
        turn_left()

# Turn left, go around the compost bin, and begin sweeping, turning when necessary, and eventually going home.
turn_left()
go_around()
while True:
    sweep()
    if finished == True:
        break;
    elif wall_in_front():
        snake()
    elif right_is_clear():
        go_around()