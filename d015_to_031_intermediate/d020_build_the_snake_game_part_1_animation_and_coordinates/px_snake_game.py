# TODO 4: Detect collision with food.
# TODO 5: Create a scoreboard.
# TODO 6: Detect collision with wall.
# TODO 7: Detect collision with self.

import time
from turtle import Screen
from snake import Snake

# Setting up the screen.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('UnfeelingRug\'s Snake Game')
screen.tracer(0)

snake = Snake()
screen.listen()

screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Left', fun=snake.left)
screen.onkey(key='Right', fun=snake.right)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
