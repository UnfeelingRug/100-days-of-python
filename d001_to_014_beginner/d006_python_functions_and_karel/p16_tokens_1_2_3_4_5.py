# My solution to the following problems on reeborg.ca:
#   Tokens 1
#   Tokens 2
#   Tokens 3
#   Tokens 4
#   Tokens 5

# Collect every token and step forward. When where are no longer any tokens, put them all down.
def collect_tokens():
    while object_here('token'):
        take()
        move()
    else:
        while carries_object('token'):
            put('token')

# Until you reach the goal, check for tokens in your current spot and then move.
while not at_goal():
    if object_here('token'):
        collect_tokens()
    move()