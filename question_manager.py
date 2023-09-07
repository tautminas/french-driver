from turtle import Turtle
from random import shuffle, choice, randint
import datetime
import pandas
import os

SPEED = 5
ACCELERATION = 10
MAX_SPEED = 55
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
FRENCH_WORDS_PATH = os.path.join(DATA_DIR, "french_words.csv")
MISTAKES_PATH = os.path.join(DATA_DIR, "mistakes.txt")


class QuestionManager:

    def __init__(self):
        self.data = pandas.read_csv(FRENCH_WORDS_PATH)
        self.questions = self.data.to_dict(orient="records")
        shuffle(self.questions)
        self.french_words = self.data['French'].tolist()

        self.correct_answer = None
        self.wrong_answer = None
        self.correct_position = None
        self.choice_set = False
        self.speed = SPEED

        self.english = Turtle()
        self.prepare_turtle(self.english)
        self.option1 = Turtle()
        self.prepare_turtle(self.option1)
        self.option2 = Turtle()
        self.prepare_turtle(self.option2)
        self.start_msg = Turtle()
        self.start_msg.goto(-25, 150)
        self.prepare_turtle(self.start_msg)
        self.controls_msg = Turtle()
        self.prepare_turtle(self.controls_msg)
        self.controls_msg.goto(-27, 128)

        # self.initialize_new_word()

        self.mistakes = []
        self.mistakes_info = Turtle()
        self.prepare_turtle(self.mistakes_info)
        screen_width = self.mistakes_info.getscreen().window_width()
        screen_height = self.mistakes_info.getscreen().window_height()
        self.mistakes_info.goto(-screen_width / 2 + 50, -screen_height / 2 + 50)

    def prepare_turtle(self, turtle):
        turtle.speed("fastest")
        turtle.penup()
        turtle.hideturtle()

    def initialize_new_word(self):
        self.correct_answer = self.questions[0]['French']  # Add "+" for debugging purposes
        self.wrong_answer = self.pick_alternative_option(self.correct_answer)
        self.correct_position = randint(0, 1)
        self.english.goto(-50, 150)
        self.english.write(f"Word: {self.questions[0]['English']}", align="center", font=("Monaco", 24, "normal"))
        self.option1.goto(510, 50)
        self.option2.goto(510, -75)
        if self.correct_position == 0:
            self.option1.write(f"{self.correct_answer}", align="left", font=("Monaco", 24, "normal"))
            self.option2.write(f"{self.wrong_answer}", align="left", font=("Monaco", 24, "normal"))
        else:
            self.option1.write(f"{self.wrong_answer}", align="left", font=("Monaco", 24, "normal"))
            self.option2.write(f"{self.correct_answer}", align="left", font=("Monaco", 24, "normal"))

    def pick_alternative_option(self, word):
        alternative = choice(self.french_words)
        while word == alternative:
            alternative = choice(self.french_words)
        return alternative

    def move_options(self):
        current_x1, current_y1 = self.option1.position()
        current_x2, current_y2 = self.option2.position()
        self.option1.clear()
        self.option2.clear()
        self.option1.goto(current_x1 - self.speed, current_y1)
        self.option2.goto(current_x2 - self.speed, current_y2)
        if self.correct_position == 0:
            self.option1.write(f"{self.correct_answer}", align="left", font=("Monaco", 24, "normal"))
            self.option2.write(f"{self.wrong_answer}", align="left", font=("Monaco", 24, "normal"))
        else:
            self.option1.write(f"{self.wrong_answer}", align="left", font=("Monaco", 24, "normal"))
            self.option2.write(f"{self.correct_answer}", align="left", font=("Monaco", 24, "normal"))

    def is_option_selected(self):
        current_x1 = self.option1.position()[0]
        if not self.choice_set and current_x1 < -410:
            self.choice_set = True
            return True
        else:
            return False

    def is_options_out(self):
        current_x1 = self.option1.position()[0]
        return current_x1 < -900

    def move_options_out(self):
        self.speed = 55

    def remove_word(self):
        self.questions.pop(0)
        self.english.clear()
        self.option1.clear()
        self.option2.clear()
        self.speed = SPEED
        self.choice_set = False

    def check_answer(self, answer):
        if answer == self.correct_position:
            return True
        else:
            self.write_mistakes_on_screen()
            return False

    def accelerate_options(self):
        if self.speed < 50:
            self.speed += ACCELERATION

    def decelerate_options(self):
        if self.speed - 10 >= SPEED:
            self.speed -= ACCELERATION

    def nitro_boost_options(self):
        self.speed = MAX_SPEED

    def reset_options_speed(self):
        self.speed = SPEED

    def write_mistakes_on_screen(self):
        self.mistakes.append(f"{self.questions[0]['English']}({self.correct_answer})")
        self.mistakes_info.clear()
        self.mistakes_info.write(f"Mistakes: {'; '.join(self.mistakes)}", align="left", font=("Monaco", 12, "italic"))

    def write_mistakes_to_file(self):
        current_datetime = datetime.datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d (%H:%M)")
        with open(MISTAKES_PATH, "a", encoding='utf-8') as file:
            file.write(f"{formatted_datetime}: {'; '.join(self.mistakes)}\n")

    def refresh_question_manager(self):
        self.speed = SPEED
        self.english.clear()
        self.option1.clear()
        self.option2.clear()
        self.mistakes_info.clear()
        self.choice_set = False
        self.mistakes = []
        self.questions = self.data.to_dict(orient="records")
        shuffle(self.questions)
