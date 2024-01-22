# TODO 7: Detect collision with self.

import time
from food import Food
from scoreboard import Scoreboard
from snake import Snake
from turtle import Screen

# Setting up the screen.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('UnfeelingRug\'s Snake Game')
screen.tracer(0)

# Create the snake, food, and scoreboard, and begin listening for input to change directions.
food = Food()
scoreboard = Scoreboard()
snake = Snake()
screen.listen()
screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Left', fun=snake.left)
screen.onkey(key='Right', fun=snake.right)

# The game loop. Update the screen, move the snake, check for collisions with food, wall, and self.
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detecting collision with food, scoring appropriately and moving the food.
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.update_score()
        snake.extend()

    # Detecting collision with the walls, ending the game if so.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 \
    or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()

    for segment in snake.segments[1:]:
        # If the snake head is colliding with the rest of its body, end the game.
        if snake.head.distance(segment) < 15:
            game_on = False
            scoreboard.game_over()
        # If the new food location is colliding with the body, find it a new position.
        if food.distance(segment) < 15:
            food.refresh()

screen.exitonclick()
