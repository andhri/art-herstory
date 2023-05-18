from tkinter import *
from game_logic_v3 import ArtGame
import main_config
# from game_options import ArtOptions
import pygame

THEME_COLOR = "#EAF6E8"

def sound_feedback(sound):
    pygame.mixer.init()
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play(loops=0)


class GameAnswers:

    def __init__(self):
        # self.art_options = ArtOptions
        # self.stan_config = main_config
        self.game_logic = ArtGame
        self.lives = 3
        self.score = 0

        self.border_1 = LabelFrame(background=THEME_COLOR, bd=10)
        self.border_1.grid(column=0, row=2, padx=20, pady=20)

        self.border_2 = LabelFrame(background=THEME_COLOR, bd=10)
        self.border_2.grid(column=1, row=2, padx=20, pady=20)

        self.lives_label = Label(text=f"Lives:{self.lives}", background=THEME_COLOR, width=10)
        # self.lives_label.config(self.stan_config.gl)
        self.lives_label.grid(column=0, row=0)

        self.score_label = Label(text=f"Score:{self.score}", background=THEME_COLOR, width=10)
        # self.score_label.config(self.stan_config.gl)
        self.score_label.grid(column=1, row=0)

    def give_feedback(self, players_choice):
        print("!!!This is the player's choice!:", players_choice)

        a = players_choice.split('-')

        if a[1] == "correct":
            if a[0] == 'option_1':
                self.border_1.config(background="green", bd=10)
            else:
                self.border_2.config(background="green", bd=10)

            # self.correct_answer_sound()
            sound_feedback(main_config.CORRECT_SOUND)
        elif a[1] == "incorrect":
            if a[0] == 'option_1':
                self.border_1.config(background="red", bd=10)
            else:
                self.border_2.config(background="red", bd=10)

            sound_feedback(main_config.INCORRECT_SOUND)

        self.score_label.config(text=f"Score:{self.score}")
        self.lives_label.config(text=f"Lives:{self.lives}")

        # self.window.after(1000, self.generate_options)

    # def option_1_answer(self):
    #     self.give_feedback(self.game_logic.check_players_choice("option_1"))
    #
    # def option_2_answer(self):
    #     self.give_feedback(self.game_logic.check_players_choice("option_2"))

