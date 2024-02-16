from turtle import Turtle

INITIAL_POSITION = (0,0)
SEGMENT_SIZE = 20
SEGMENT_SHAPE = "square"
SEGMENT_COLOR = "white"
MOVE_DISTANCE = 20
HEADING = {
    "UP": 90,
    "DOWN": 270,
    "LEFT": 180,
    "RIGHT": 0
}


class Snake:

    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        initial_x = INITIAL_POSITION[0]
        initial_y = INITIAL_POSITION[1]
        initial_position = (initial_x, initial_y)
        for turtle in range(3):
            self.add_segment(initial_position)
            initial_x -= SEGMENT_SIZE

    def add_segment(self, position):
        new_segment = Turtle(shape=SEGMENT_SHAPE)
        new_segment.color(SEGMENT_COLOR)
        new_segment.penup()
        new_segment.goto(position)
        self.body.append(new_segment)

    def extend(self):
        self.add_segment(self.body[-1].position())

    def move(self):
        for snake_segment in range(len(self.body) - 1, 0, -1):
            new_x = self.body[snake_segment - 1].xcor()
            new_y = self.body[snake_segment - 1].ycor()
            self.body[snake_segment].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def snake_heading(self):
        return self.head.heading()

    def set_snake_heading(self, angle):
        self.head.setheading(to_angle=angle)

    def go_up(self):
        if self.snake_heading() != HEADING["DOWN"]:
            self.set_snake_heading(HEADING["UP"])

    def go_down(self):
        if self.snake_heading() != HEADING["UP"]:
            self.set_snake_heading(HEADING["DOWN"])

    def go_left(self):
        if self.snake_heading() != HEADING["RIGHT"]:
            self.set_snake_heading(HEADING["LEFT"])

    def go_right(self):
        if self.snake_heading() != HEADING["LEFT"]:
            self.set_snake_heading(HEADING["RIGHT"
                                           ""])
