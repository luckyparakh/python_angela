from SnakeGame.snake import Snake
from turtle import Screen
from time import sleep
from SnakeGame.food import Food
from SnakeGame.scoreboard import ScoreBoard

WIDTH = 600
HEIGHT = 600
score = 0
screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")
# Without this snake movement will be like a caterpillar. Tracer is off by calling below & to update screen
# call screen.update()
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
sb = ScoreBoard()
sb.write_score()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)
    snake.movement()
    if snake.head.distance(food) < 15:
        food.refresh()
        sb.write_score()
        snake.add_segment()
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        game_is_on = False
        sb.game_over()
    if snake.hit_segment():
        game_is_on = False
        sb.game_over()

screen.exitonclick()
