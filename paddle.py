from turtle import Turtle


class Paddle(Turtle):
    
    def __init__(self,x,y):
        super().__init__()

        self.paddle =Turtle()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x, y)
        self.position


    def goUp(self):
        yposs = self.ycor() + 20
        self.goto(self.xcor(), yposs)


    def goDown(self):

        yposs = self.ycor() - 20
        self.goto(self.xcor(), yposs)

    def check(self):
        yposs = self.ycor()
        if yposs > 260:
            self.goto(self.xcor(), 260)
        if yposs < -260:
            self.goto(self.xcor(), -260)