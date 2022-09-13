import time
from turtle import Screen, Turtle

import timer as timer

from models import Snake
from models.food import Food
from models.scoreboard import Scoreboard

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

high_score = 0
with open('high_scores.txt', mode='r') as file:
    high_score = file.read()

screen.bgcolor('black')
screen.title("My Snake.py Game")
screen.tracer(0)
snake_length = 3
snake = Snake.Snake()
food = Food()
scoreboard = Scoreboard(high_score=int(high_score))

screen.listen()

global game_is_on
game_is_on = True


def restart():
    print('restart')
    snake.restart()


screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
screen.onkey(restart, 'r')


def is_colliding_with_border():
    if abs(snake.get_head().xcor()) > (SCREEN_WIDTH // 2) - 20 or \
            abs(snake.get_head().ycor()) > (SCREEN_HEIGHT // 2) - 20:
        return True

    return False


def is_colliding_with_tail():
    for idx in range(1, len(snake.segments)):
        if snake.head.distance(snake.segments[idx]) < 10:
            return True

    return False


while game_is_on:
    snake.move()
    screen.update()
    time.sleep(0.1)

    game_is_on = not is_colliding_with_tail()

    if game_is_on:
        game_is_on = not is_colliding_with_border()

    if not game_is_on:
        scoreboard.reset()
        snake.restart()
        game_is_on = True

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.relocate()
        snake.eat()
        scoreboard.increase_score()
        scoreboard.update_score()


# game_over = Turtle()
# game_over.color('white')
# game_over.write('Game Over!', True, align='center', font=('Courier', 25, 'bold'))


screen.exitonclick()