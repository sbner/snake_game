from turtle import Turtle
from random import randint

SHAPE_SIZE = (.5,.5)


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=SHAPE_SIZE[0], stretch_len=SHAPE_SIZE[1])
        self.color("blue")
        self.speed("fastest")
        self.spawn()

    def spawn(self):
        location = (float(randint(-280, 280)), float(randint(-280, 280)))
        self.teleport(location[0], location[1])