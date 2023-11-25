from turtle import Screen 
from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time

SCREEN_POSITIVE_SIZE = 280
SCREEN_NEGATIVE_SIZE = -280

# init screen in the beginning of the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snack Game")
screen.bgcolor("black")
screen.tracer(20)

scoreboard = Scoreboard()
snake = Snake()
food = Food()

# screen listenner
screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_right, "Right")
screen.onkey(snake.move_left, "Left")

game_is_on = True
while game_is_on:

    screen.update() #refresh the screen
    time.sleep(0.25)
    snake.constant_move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increas_score()

    if snake.head.xcor() > SCREEN_POSITIVE_SIZE or snake.head.xcor() < SCREEN_NEGATIVE_SIZE or snake.head.ycor() > SCREEN_POSITIVE_SIZE or snake.head.ycor() < SCREEN_NEGATIVE_SIZE:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()