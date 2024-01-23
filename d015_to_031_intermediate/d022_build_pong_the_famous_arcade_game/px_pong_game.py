import time
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
from turtle import Screen

# Set up the screen with size, background color, title, paddles, etc.
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('UnfeelingRug\'s Pong Game')
screen.tracer(0)
ball = Ball()
scoreboard = Scoreboard()
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

# Add the event listener, watch for player input.
screen.listen()
screen.onkey(key='w', fun=l_paddle.up)
screen.onkey(key='s', fun=l_paddle.down)
screen.onkey(key='Up', fun=r_paddle.up)
screen.onkey(key='Down', fun=r_paddle.down)

# Run the game, launch the ball, call for bounces or score changes when appropriate.
game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with the upper and lower walls.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce(hit='wall')

    # Detect collision with the paddles.
    if (ball.xcor() > 320 and ball.distance(r_paddle) < 50) \
    or (ball.xcor() < -320 and ball.distance(l_paddle) < 50):
        ball.bounce(hit='paddle')

    # Detect when the ball misses on the left or right sides.
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.update_score('L')
    elif ball.xcor() < -380:
        ball.reset()
        scoreboard.update_score('R')
    if scoreboard.lscore >= 7 or scoreboard.rscore >= 7:
        scoreboard.game_over()
        game_on = False

screen.exitonclick()
