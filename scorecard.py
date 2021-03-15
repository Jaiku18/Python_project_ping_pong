from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")
GameFont = ("Courier", 40, "normal")


class ScoreCard(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x, y)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(self.score, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self, player):
        self.goto(0, 0)
        self.write(f"GAME OVER {player} wins", align=ALIGNMENT, font=GameFont)