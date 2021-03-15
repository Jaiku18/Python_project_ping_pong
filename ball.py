from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.xstep = 10
        self.ystep = 10
        self.speed = 0.05

    def move(self):
        new_xcor = self.xcor() + self.xstep
        new_ycor = self.ycor() + self.ystep

        self.goto(new_xcor, new_ycor)

    def checkBounce(self):
        self.ystep *= -1

    def checkCollision(self):
        self.xstep *= -1
        self.speed *= 0.9
