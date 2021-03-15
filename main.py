from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scorecard import ScoreCard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")

screen.title('Ping Pong')
screen.tracer(0)
paddleRight = Paddle(360, 0)
paddleLeft = Paddle(-360, 0)

screen.update()
screen.tracer(1)
ball = Ball()

rightScoreCard = ScoreCard(100, 200)
leftScoreCard = ScoreCard(-100, 200)
speed = 0.05
game_is_on = True
while game_is_on:
    screen.listen()
    screen.onkey(paddleRight.goUp, 'Up')
    screen.onkey(paddleRight.goDown, 'Down')
    screen.onkey(paddleLeft.goUp, 'w')
    screen.onkey(paddleLeft.goDown, 's')
    ball.move()
    time.sleep(ball.speed)
    screen.update()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.checkBounce()

    if ball.distance(paddleRight) < 50 and ball.xcor() > 340:
        ball.checkCollision()

    if ball.distance(paddleLeft) < 50 and ball.xcor() < -340:
        ball.checkCollision()

    if ball.xcor() > 350:
        leftScoreCard.increase_score()
        ball.speed = 0.1
        time.sleep(0.5)
        ball.goto(0, 0)
        ball.checkCollision()

    if ball.xcor() < -350:
        rightScoreCard.increase_score()
        ball.speed = 0.1
        time.sleep(0.5)
        ball.goto(0, 0)
        ball.checkCollision()
    if rightScoreCard.score >= 5:
        rightScoreCard.game_over('Player 2')
        game_is_on = False
    if leftScoreCard.score >= 5:
        leftScoreCard.game_over('Player 1')
        game_is_on = False

    paddleRight.check()
    paddleLeft.check()

screen.exitonclick()
