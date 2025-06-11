from turtle import Screen
from snake import Snake
from food import Food
from specialfood import Special_food
from scoreboard import Scoreboard
import builtins
import time

screen = Screen()
screen.setup(width=600, height = 600)
screen.bgcolor("green")
screen.title("My Snake Game")
screen.tracer(0)

#game objects
snake = Snake()   
food = Food()
special_food = Special_food()
scoreboard = Scoreboard()

#share snaeke with other modules
builtins.snake = snake

#share the game state
game_is_on = True
builtins.game_is_on = True

#keyboard binding
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

while game_is_on:
    screen.update()
    time.sleep(0.15)       #1s delay
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with special food
    if special_food.isvisible() and snake.head.distance(special_food)<15:
        special_food.hideturtle()
        special_food.timer.stop()
        special_food.schedule_spawn()
        snake.extend()
        scoreboard.increase_score(2)

    #Detect collison with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_is_on = False
        builtins.game_is_on = False
        special_food.timer.stop()
        scoreboard.game_over()
        
    #Detect collision with tail
    for segment in snake.segments[1:]:      #slices after the head
        if snake.head.distance(segment)<10:
            game_is_on = False
            builtins.game_is_on = False
            special_food.timer.stop()
            scoreboard.game_over()

screen.exitonclick()

