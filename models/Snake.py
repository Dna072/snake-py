from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self, start_length=3):
        self.segments = []
        self.length = start_length
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        start_x = 0
        for _ in range(self.length):
            segment = Turtle(shape='square')
            segment.penup()
            segment.color('white')
            segment.goto(start_x, 0)
            start_x -= 20
            self.segments.append(segment)

        self.head = self.segments[0]

    def restart(self):
        for segment in self.segments:
            segment.goto(x=1000, y=1000)

        self.segments = []
        self.create_snake()

    def move(self):
        for i in reversed(range(1, len(self.segments))):
            segment = self.segments[i]
            next_x = self.segments[i - 1].position()[0]
            next_y = self.segments[i - 1].position()[1]
            segment.goto(next_x, next_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        # current_angle = head.heading()
        # print(f'current heading: {current_angle}')
        # head.setheading(current_angle + 90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        # current_angle = head.heading()
        # print(f'current heading: {current_angle}')
        # head.setheading(current_angle - 90)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def eat(self):
        segment = Turtle(shape='square')
        segment.penup()
        segment.color('white')
        self.segments.append(segment)

    def get_head(self):
        return self.head
