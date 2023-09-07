from turtle import Turtle

HEIGHT = 250
LEFT = 180
SPEED = 5
ACCELERATION = 10
MAX_SPEED = 55


class Road(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.hideturtle()
        self.speed = SPEED

        self.create_edges()

        self.divisions = []
        self.create_divisions()

    def create_edges(self):
        screen_width = self.getscreen().window_width()
        self.pensize(5)
        self.penup()
        self.goto(-screen_width / 2, HEIGHT / 2)
        self.pendown()
        self.goto(screen_width / 2, HEIGHT / 2)
        self.penup()
        self.goto(-screen_width / 2, -HEIGHT / 2)
        self.pendown()
        self.goto(screen_width / 2, -HEIGHT / 2)
        self.penup()

    def create_divisions(self):
        screen_width = self.getscreen().window_width()
        starting_position = -(screen_width / 2) + 20
        num_divisions = (screen_width // 75) + 3
        self.backward(-screen_width / 2 + 50)
        for i in range(num_divisions):
            self.add_division((starting_position + 75 * i, 0))

    def add_division(self, position):
        new_division = Turtle("square")
        new_division.turtlesize(stretch_wid=0.3, stretch_len=1)
        new_division.color("black")
        new_division.setheading(LEFT)
        new_division.penup()
        new_division.goto(position)
        self.divisions.append(new_division)

    def move_divisions(self):
        screen_width = self.getscreen().window_width()
        boundary = -(screen_width / 2) - 30
        divisions_to_append = []
        for division in self.divisions:
            division.forward(self.speed)
            if division.xcor() < boundary:
                divisions_to_append.append(division)
        for division in divisions_to_append:
            division.goto(self.divisions[-1].xcor() + 75, 0)
            self.divisions.append(self.divisions.pop(0))

    def accelerate(self):
        if self.speed < MAX_SPEED:
            self.speed += ACCELERATION

    def decelerate(self):
        if self.speed - ACCELERATION >= SPEED:
            self.speed -= ACCELERATION

    def nitro_boost(self):
        self.speed = MAX_SPEED

    def reset_speed(self):
        self.speed = SPEED
