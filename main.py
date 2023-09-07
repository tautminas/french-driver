from turtle import Screen, Terminator
from car import Car
from road import Road
from question_manager import QuestionManager
from scoreboard import Scoreboard
import time

START_FONT = ("Press Start 2P", 24, "bold")
CONTROLS_FONT = ("Press Start 2P", 12, "bold")


def accelerate():
    road.accelerate()
    question_manager.accelerate_options()


def decelerate():
    road.decelerate()
    question_manager.decelerate_options()


def nitro_boost():
    road.nitro_boost()
    question_manager.nitro_boost_options()


def handbrake():
    road.reset_speed()
    question_manager.reset_options_speed()


def start_game():
    global game_is_on
    game_is_on = True


screen = Screen()
screen.setup(width=1000, height=500)
# You shall not access protected members 🧙‍♂️! Unless it is the only way to disable resizability.
screen.cv._rootwindow.resizable(False, False)
screen.bgcolor("#C8FFE0")
screen.title("French Driver")
screen.listen()

screen.tracer(0)
road = Road()
scoreboard = Scoreboard()
question_manager = QuestionManager()
car = Car()
screen.tracer(1)

screen.listen()
# Main controls
screen.onkey(car.shift_to_lane_1, "Up")
screen.onkey(car.shift_to_lane_2, "Down")
screen.onkey(nitro_boost, "Right")
screen.onkey(handbrake, "Left")
# Optionals controls
screen.onkeypress(car.up, "w")
screen.onkeypress(car.down, "s")
screen.onkey(accelerate, "d")
screen.onkey(decelerate, "a")
screen.onkey(nitro_boost, "space")
# Signal to play
screen.onkey(start_game, "Return")

is_choice_correct = None
game_is_on = False
first_play = True
# Game will be closed with exit button
try:
    while True:
        question_manager.english.clear()
        question_manager.controls_msg.write("Control the car with the arrow keys (←;↑;→;↓).",
                                            align="center", font=CONTROLS_FONT)
        # Display flashing intro message
        while not game_is_on:
            question_manager.start_msg.clear()
            if first_play:
                question_manager.start_msg.write("Ready to Play? Press Enter!", align="center", font=START_FONT)
            else:
                question_manager.start_msg.write("Ready to Restart? Press Enter!", align="center", font=START_FONT)
            screen.update()
            if game_is_on is True:
                continue
            time.sleep(0.5)
            question_manager.start_msg.clear()
            screen.update()
            if game_is_on is True:
                continue
            time.sleep(0.5)
        question_manager.controls_msg.clear()
        # Prepare for a replay
        if not first_play:
            screen.tracer(0)
            scoreboard.refresh_scoreboard()
            question_manager.refresh_question_manager()
            road.reset_speed()
            screen.tracer(1)
        question_manager.start_msg.clear()
        # Start playing
        question_manager.initialize_new_word()
        while game_is_on:
            screen.update()
            time.sleep(0.1)
            screen.tracer(0)
            road.move_divisions()
            question_manager.move_options()
            if question_manager.is_option_selected():
                if car.position()[1] > 0:
                    is_choice_correct = question_manager.check_answer(0)
                else:
                    is_choice_correct = question_manager.check_answer(1)
                question_manager.move_options_out()
                scoreboard.increase_score()
                if not is_choice_correct:
                    scoreboard.remove_life()
                    if scoreboard.is_lost():
                        scoreboard.write_high_score_to_file()
                        question_manager.write_mistakes_to_file()
                        game_is_on = False
                        first_play = False
            if question_manager.is_options_out():
                question_manager.remove_word()
                question_manager.reset_options_speed()
                road.reset_speed()
                question_manager.initialize_new_word()
                if len(question_manager.questions) == 0:
                    scoreboard.write_high_score_to_file()
                    question_manager.write_mistakes_to_file()
                    game_is_on = False
                    first_play = False
            screen.tracer(1)
except Terminator:
    print("Turtle graphics window was closed by the escape button. Thank you for playing :)!")
