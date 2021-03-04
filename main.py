from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from playsound import playsound
from scoreboard import Scoreboard

# Global Variables
BG_COLOR = "black"

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor(BG_COLOR)
screen.title("Pong Game")
screen.tracer(0)
screen.listen()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

is_game_on = True

while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()
    # Detect collision with wall
    if ball.does_collide_with_wall():
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        playsound("ball.mp3", False)
        ball.bounce_x()

    # Detect when ball misses the paddle
    # Detect R_Paddle Miss
    elif ball.xcor() > 390:
        scoreboard.increase_left()
        ball.reset_ball()

    # Detect L_Paddle Miss
    elif ball.xcor() < -390:
        scoreboard.increase_right()
        ball.reset_ball()

screen.exitonclick()
