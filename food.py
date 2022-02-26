from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.new_location()
        self.color("blue")
        self.speed("fastest")

    def new_location(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))