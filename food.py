from turtle import Turtle
import random

SCREEN_POSITIVE_SIZE = 280
SCREEN_NEGATIVE_SIZE = -280

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        # self.shapesize(0.5, 0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(SCREEN_NEGATIVE_SIZE, SCREEN_POSITIVE_SIZE)
        random_y = random.randint(SCREEN_NEGATIVE_SIZE, SCREEN_POSITIVE_SIZE)
        self.goto(random_x, random_y)