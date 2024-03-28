from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600,600)
screen.bgpic("Garden-Background.jpg")
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

score = 0
game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(0.0666)
    snake.move()
    if snake.head.distance(food) < 18:
        food.refresh()
        snake.add_snake()
        scoreboard.increase_score()


    if snake.head.xcor() >= 270 or snake.head.xcor() <= -270 or snake.head.ycor() >= 270 or snake.head.ycor() <=  -270:
        if snake.head.ycor() < 20 and snake.head.ycor() > -20 and snake.head.heading() == 0:
            snake.head.teleport(x= -270, y=0)
        elif snake.head.ycor() < 20 and snake.head.ycor() > -20 and snake.head.heading() == 180:
            snake.head.teleport(x= 270, y=0)
        else:
            scoreboard.update_highscore()
            snake.reset()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            snake.reset()
            scoreboard.update_highscore()










screen.exitonclick()
