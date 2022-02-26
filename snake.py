import time
from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    """ Welcome students This is the snek class """

    def __init__(self):
        self.segments = []

        for x in range(3):
            self.segments.append(Turtle("square"))
            self.segments[x].penup()
            self.segments[x].color("white")
            self.segments[x].goto((x * -20), 0)

        self.head = self.segments[0]

    def new_segment(self):
        tempSegment = Turtle("square")
        tempSegment.penup()
        tempSegment.color("white")
        tempSegment.goto(self.segments[len(self.segments)-1].xcor(), self.segments[len(self.segments)-1].ycor())
        self.segments.append(tempSegment)


    def move_forward(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
        time.sleep(0.1)

    def up(self):
        if self.head.heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)

