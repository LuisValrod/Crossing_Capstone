COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random
class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.color(COLORS[random.randint(0, len(COLORS)-1)])
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()

    def move(self):
        self.goto(self.xcor() - STARTING_MOVE_DISTANCE, self.ycor())
