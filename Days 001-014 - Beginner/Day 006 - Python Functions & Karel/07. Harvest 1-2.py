# My solution to the following problems on reeborg.ca:
#   Harvest 1
#   Harvest 2

# At the end of a row, set up for a new row on your left.
def snake_left():
    turn_left()
    move()
    turn_left()
    move()

# At the end of a row, set up for a new row on your right.
def snake_right():
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()

# Move along the row, harvesting every carrot in your path before moving on.
def harvest_row():
    for i in range(6):
        while object_here('carrot'):
            take()
        move()
    
# Hardcoding set up and getting into position at the farm.
turn_left()
move()
move()
turn_left()
turn_left()
turn_left()
move()
move()

# Call for Reeborg to cycle through harvesting and snaking to higher rows, so everything gets harvested.
for i in range(3):
    harvest_row()
    snake_left()
    harvest_row()
    snake_right()