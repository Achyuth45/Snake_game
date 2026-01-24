from turtle import Screen
import time
from snake_class import Snake
from food import Food
from score_board import Score
s=Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("MY SNAKE GAME")
s.tracer(0)

snake=Snake()
food=Food()
score=Score()


s.listen()
s.onkey(snake.up,"Up")
s.onkey(snake.down,"Down")
s.onkey(snake.right,"Right")
s.onkey(snake.left,"Left")

over=True
while over:
    s.update()
    time.sleep(0.2)
    snake.move()
    if snake.head.distance(food) < 15:
        food.rnd_position()
        snake.increase()
        score.increase_score()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() >280 or snake.head.ycor() < -280:
        score.game_over()
        over = False
    if snake.tail_collision():
        over = False
        score.game_over()




s.exitonclick()