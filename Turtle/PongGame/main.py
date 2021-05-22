from turtle import Screen
from PongGame.bat import Bat
from PongGame.ball import Ball
from time import sleep
from PongGame.scoreboard import ScoreBoard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Ping Pong Game")
screen.listen()
screen.tracer(0)
l_bat = Bat((-280, 20))
r_bat = Bat((280, 20))
ball = Ball()
sb = ScoreBoard()
sb.write_score()

screen.onkeypress(r_bat.up, "Up")
screen.onkeypress(r_bat.down, "Down")
screen.onkeypress(l_bat.up, "a")
screen.onkeypress(l_bat.down, "z")

is_game_on = True
while is_game_on:
    screen.update()
    sleep(ball.move_speed)
    ball.movement()

    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()
    if (ball.distance(r_bat) < 50 and ball.xcor() > 260) or (ball.distance(l_bat) < 50 and ball.xcor() < -260):
        ball.bounce_x()
    if ball.xcor() > 290:
        ball.reset()
        sb.lp_score += 1
        sb.write_score()
    if ball.xcor() < -290:
        ball.reset()
        sb.rp_score += 1
        sb.write_score()
screen.exitonclick()
