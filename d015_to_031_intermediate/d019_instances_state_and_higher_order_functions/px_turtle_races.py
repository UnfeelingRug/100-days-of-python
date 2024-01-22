from random import randint
from turtle import Turtle, Screen

# Establish a list of usable colors, and a dictionary for turtles.
turtle_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
turtles = []
is_race_on = False


# Create the turtle, lift the pen, set their color and put them at the starting line.
def place_turtle(name, y):
    new_turtle = Turtle(shape='turtle')
    new_turtle.up()
    new_turtle.color(name)
    new_turtle.setpos(-230, y)
    turtles.append(new_turtle)


# Create the screen, 500x400.
screen = Screen()
screen.setup(width=500, height=400)

# Get the user to make a bet, then place the seven turtles at the starting line.
bet = screen.textinput(title="Which turtle will win the race?",
                       prompt="Pick a turtle! They're named after the rainbow.")
for i in range(7):
    place_turtle(turtle_colors[i], -40 * i + 120)

# Once the player has set a bet, enable the race and get the turtles moving randomly.
# When a winner is decided, inform the user and stop the race.
if bet:
    is_race_on = True
while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == bet:
                print(f'Congratulations, the {winning_color} turtle won the race!')
            else:
                print(f'Too bad! The {winning_color} turtle won!')

        distance = randint(0, 10)
        turtle.forward(distance)


# Once everything is done, close the program when clicking the window.
screen.exitonclick()
