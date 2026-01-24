from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.rnd_position()
    def rnd_position(self):
        rnd_x = random.randint(-280,280)
        rnd_y = random.randint(-280, 280)
        self.goto(rnd_x,rnd_y)