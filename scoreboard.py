from turtle import Turtle
import os
import sys

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
HIGH_SCORE_FONT = ("Courier", 12, "normal")
BASE_PATH = os.path.abspath(os.path.dirname(sys.argv[0]))
if os.path.basename(BASE_PATH) == 'dist':
    BASE_PATH = os.path.abspath(os.path.join(BASE_PATH, os.pardir))
ASSETS_DIR = os.path.join(BASE_PATH, "assets")
HEART_PATH = os.path.join(ASSETS_DIR, "heart.gif")
DATA_DIR = os.path.join(BASE_PATH, "data")
HIGH_SCORE_PATH = os.path.join(DATA_DIR, "high_score.txt")


class Scoreboard:

    def __init__(self):
        self.score = 0

        self.distance = Turtle()
        self.prepare_turtle(self.distance)

        self.screen = self.distance.getscreen()
        self.screen_width = self.screen.window_width()
        self.screen_height = self.screen.window_height()

        # Write score
        self.distance.goto(self.screen_width / 2 - 200, self.screen_height / 2 - 50)
        self.distance.color("black")
        self.distance.write(arg=f"Distance: {self.score}/1000", align=ALIGNMENT, font=FONT)

        # Write lives
        self.lives = Turtle()
        self.prepare_turtle(self.lives)
        self.lives.goto(-self.screen_width / 2 + 80, self.screen_height / 2 - 50)
        self.lives.write(arg="Lives:", align=ALIGNMENT, font=FONT)

        self.screen.register_shape(HEART_PATH)
        self.hearts = []
        self.create_hearts()

        self.high_score = 0
        self.read_high_score_from_file()
        self.high_score_turtle = Turtle()
        self.prepare_turtle(self.high_score_turtle)
        self.high_score_turtle.goto(self.screen_width / 2 - 200, self.screen_height / 2 - 80)
        self.high_score_turtle.write(arg=f"High score: {self.high_score}", align=ALIGNMENT, font=HIGH_SCORE_FONT)

    def prepare_turtle(self, turtle):
        turtle.speed("fastest")
        turtle.penup()
        turtle.hideturtle()

    def create_hearts(self):
        starting_x = - self.screen_width / 2 + 155
        starting_y = self.screen_height / 2 - 32
        for i in range(3):
            self.add_heart((starting_x + 40 * i, starting_y))

    def add_heart(self, position):
        new_heart = Turtle()
        new_heart.shape(HEART_PATH)
        new_heart.penup()
        new_heart.goto(position)
        self.hearts.append(new_heart)

    def increase_score(self):
        self.score += 1
        self.distance.clear()
        self.distance.goto(self.screen_width / 2 - 200, self.screen_height / 2 - 50)
        self.distance.color("black")
        self.distance.write(arg=f"Distance: {self.score}/1000", align=ALIGNMENT, font=FONT)

    def remove_life(self):
        self.hearts[-1].hideturtle()
        self.hearts.pop()

    def is_lost(self):
        if len(self.hearts) == 0:
            return True
        else:
            return False

    def read_high_score_from_file(self):
        try:
            with open(HIGH_SCORE_PATH, 'r') as high_score:
                self.high_score = int(high_score.read())
        except FileNotFoundError:
            with open(HIGH_SCORE_PATH, 'w') as high_score:
                initial_score = 0
                high_score.write(str(initial_score))
                self.high_score = initial_score
        except ValueError:
            with open(HIGH_SCORE_PATH, 'w') as high_score:
                initial_score = 0
                high_score.write(str(initial_score))
                self.high_score = initial_score

    def write_high_score_to_file(self):
        if self.score > self.high_score:
            with open(HIGH_SCORE_PATH, "w") as file:
                file.write(f"{self.score}")

    def refresh_scoreboard(self):
        self.score = 0
        self.read_high_score_from_file()
        self.high_score_turtle.clear()
        self.high_score_turtle.write(arg=f"High score: {self.high_score}", align=ALIGNMENT, font=HIGH_SCORE_FONT)
        self.distance.clear()
        self.distance.write(arg=f"Distance: {self.score}/1000", align=ALIGNMENT, font=FONT)
        self.create_hearts()
