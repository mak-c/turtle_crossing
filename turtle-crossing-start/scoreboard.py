from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-210, 250)
        self.level = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        game_over_turtle = Turtle()
        game_over_turtle.hideturtle()
        game_over_turtle.penup()
        game_over_turtle.goto(0, 0)
        game_over_turtle.color("white")
        game_over_turtle.write(f"GAME OVER (click to close)", align="center", font=FONT)
