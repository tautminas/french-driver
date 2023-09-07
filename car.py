from turtle import Turtle
from road import HEIGHT

CAR_SHAPE = (
    (0, 5), (0, 3), (-5, 3), (-5, -3), (0, -3), (0, -5), (4, -5), (4, -3),
    (5, -3), (5, -2), (4, -2), (4, 2), (5, 2), (5, 3), (4, 3), (4, 5)
)


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.screen = self.getscreen()
        self.screen.register_shape("car", CAR_SHAPE)
        self.turtlesize(stretch_wid=4, stretch_len=8)
        self.shape("car")
        self.color("#614BC3")
        self.penup()
        self.speed("fastest")

        self.screen_width = self.getscreen().window_width()
        self.goto(-self.screen_width / 2 + 50, 0)

    def up(self):
        current_x, current_y = self.position()
        upper_boundary = (HEIGHT / 2) - 10
        if current_y < upper_boundary:
            new_y = current_y + 10
            self.goto(current_x, new_y)

    def down(self):
        current_x, current_y = self.position()
        lower_boundary = -(HEIGHT / 2) + 25
        if current_y > lower_boundary:
            new_y = current_y - 10
            self.goto(current_x, new_y)

    def shift_to_lane_1(self):
        self.goto(-self.screen_width / 2 + 50, 62)

    def shift_to_lane_2(self):
        self.goto(-self.screen_width / 2 + 50, -62)
