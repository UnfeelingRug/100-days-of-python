# My solution to the following problems on reeborg.ca:
#   Newspaper 0
#   Newspaper 1

# Go up the defined number of stairs.
def up_stairs(x):
    for i in range(x):
        turn_left()
        move()
        turn_left()
        turn_left()
        turn_left()
        move()
        move()
        
# Go down the defined number of stairs.
def down_stairs(x):
    for i in range(x):
        move()
        move()
        turn_left()
        move()
        turn_left()
        turn_left()
        turn_left()

# Hard-coding the rest of the movement, calling for stairs when I can.     
take()
up_stairs(3)
put()
# Take the tokens left, but leave the newspaper.
while object_here('token'):
    take('token')
turn_left()
turn_left()
down_stairs(3)