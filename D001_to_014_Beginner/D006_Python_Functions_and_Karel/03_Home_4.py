# My solution to the following problem on reeborg.ca:
#   Home 4

# To move across one L-section from end to end.
def L():
    move()
    move()
    move()
    turn_left()
    move()
    move()
    move()
    
# To prepare yourself for the next L-section.
def nextQuarter():
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()

# Simply call the functions in the right order to get home.
L()
nextQuarter()
L()
nextQuarter()
L()
nextQuarter()
L()