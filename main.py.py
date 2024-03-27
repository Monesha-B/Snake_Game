from turtle import Screen
import time
from snake import Snake
from food import Food
from score import ScoreBoard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    snake.move()

    if snake.head.distance(food) <= 6:
        food.refresh()
        score.increase_score()

    if snake.head.xcor() >= 290 or snake.head.xcor() <= -290 or snake.head.ycor() >= 283 or snake.head.ycor() <= -290:
        game_is_on = False
        snake.extend()
        score.increase_score()

        # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

        # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            game_is_on = False
            score.game_over()


screen.exitonclick()
