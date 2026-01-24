from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.update_score()
    def update_score(self):
        self.write(f"SCORE = {self.score}", move=False, align="center", font=("arial", 10, "normal"))
    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_score()
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER..", move=False, align="center", font=("arial", 10, "normal"))