import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self, env_width=600, env_height=600):
        super().__init__()
        self.env_width = env_width
        self.env_height = env_height
        self.shape('circle')
        self.color('blue')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed('fastest')
        self.relocate()

    def relocate(self):
        rand_x = random.randint(-(self.env_width // 2)+30, (self.env_width // 2)-30)
        rand_y = random.randint(-(self.env_height // 2)+30, (self.env_height // 2)-30)
        self.goto(rand_x, rand_y)



