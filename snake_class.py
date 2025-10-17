from turtle import Turtle
COORDINATES=[(0,0),(-20,0),(-40,0)]
UP=90
DOWN=270
RIGHT=0
LEFT=180
class Snake:
    def __init__(self):
        self.segment=[]
        self.create_snake()
        self.head=self.segment[0]

    def create_snake(self):
        for position in COORDINATES:
            self.extend(position)

    def extend(self,position):
            t = Turtle("square")
            t.penup()
            t.color("white")
            t.goto(position)
            self.segment.append(t)

    def increase(self):
        self.extend(self.segment[-1].position())

    def move(self):
        for seg in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg - 1].xcor()
            new_y = self.segment[seg - 1].ycor()
            self.segment[seg].goto(new_x, new_y)
        self.segment[0].fd(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def tail_collision(self):
        for box in range(1,len(self.segment)):

            if self.head.distance(self.segment[box]) < 10:
                return True
        return False

