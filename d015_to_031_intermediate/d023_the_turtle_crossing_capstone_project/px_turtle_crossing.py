import time
from turtle import Screen
from player import Player
from random import randint
from car_manager import CarManager
from scoreboard import Scoreboard

# Get the screen set up, including the player, scoreboard, and car manager.
# Begin listening for player input to move the Turtle forward.
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()
screen.listen()
screen.onkeypress(key='w', fun=player.move)

# Run the game, randomly spawn cars, and make them move.
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if randint(1, 7) == 1:
        car_manager.add_car()
    car_manager.move_cars()

    # Check if the player has reached the end, increasing their score and resetting the screen for the next stage.
    if player.check_pos():
        scoreboard.update_score()
        car_manager.increase_stage()
        player.reset()

    # Check the player's collision with each car, and cause a game over if they're too close.
    for car in car_manager.cars:
        if player.distance(car) < 27 and abs(player.ycor() - car.ycor()) < 17:
            game_is_on = False
            scoreboard.game_over()

# Freeze the game at the last frame, and exit once the player clicks.
screen.exitonclick()
