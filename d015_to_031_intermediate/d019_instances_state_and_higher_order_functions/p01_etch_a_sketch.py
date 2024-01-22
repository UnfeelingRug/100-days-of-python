from turtle import Turtle, Screen


def move_forwards():
    franklin.forward(10)


def move_backwards():
    franklin.backward(10)


def turn_left():
    franklin.left(10)


def turn_right():
    franklin.right(10)


def reset():
    franklin.up()
    franklin.setpos(0, 0)
    screen.resetscreen()
    franklin.down()


# Bring in a Turtle and a Screen, start listening for input.
franklin = Turtle()
screen = Screen()
screen.listen()

# Move Franklin depending on the user's input, resetting his position and drawing history with C.
screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='c', fun=reset)


# Once everything is done, close the program when clicking the window.
screen.exitonclick()
