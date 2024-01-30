import pandas
from turtle import Screen, Turtle

# Create the screen with the US States image (a Turtle) as the background.
screen = Screen()
screen.setup(width=725, height=491)
screen.title("U.S. States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
background = Turtle(image)

# Get the info from the spreadsheet with state data in it.
data = pandas.read_csv('50_states.csv')
all_states = data.state.tolist()

while len(all_states) > 0:
    # Get the player's input to name a state. Tell them how many they have.
    answer_state = screen.textinput(title=f'{50-len(all_states)}/50 States guessed', prompt='Name a state!').title()

    # If they name one correctly, label the state in the (approximate) correct spot on the map.
    # Remove the state from the list of all states so it cannot be guessed again.
    if answer_state in all_states:
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        all_states.remove(answer_state)

    # If the user types "Exit" let them close the game.
    elif answer_state == 'Exit':
        break

data = pandas.DataFrame(all_states)
data.to_csv('missed_states.csv')
