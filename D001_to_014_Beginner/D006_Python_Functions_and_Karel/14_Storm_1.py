# My solution to the following problems on reeborg.ca:
#   Storm 1

# Define the ability to turn any given number of times.
def turn_x(x):
    for i in range(x):
        turn_left()
        
# Make Reeborg walk up the path, picking up every leaf, then turn around and come home when he reaches the end.
for i in range(2):
    while front_is_clear():
        move() 
        while object_here('leaf'):
            take('leaf')
    else:
        turn_x(2)

#Turn towards the compost bin once home, and throw all the leaves into it.
turn_left()
while carries_object('leaf'):
    toss('leaf')