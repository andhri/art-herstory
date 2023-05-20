from tkinter import *
from game_logic_v4 import ArtGame
import main_config
from game_options import ArtOptions
import pygame
from display import DisplayConfig
import main_config
from parent_interface import Parent


def sound_feedback(sound):
    pygame.mixer.init()
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play(loops=0)


class GameAnswers:

    def __init__(self, parent: Parent, game_logic: ArtGame, display: DisplayConfig):
        self.art_options = ArtOptions
        self.answers = GameAnswers
        # self.stan_config = main_config
        self.game_logic = game_logic
        self.game_display = display
        self.parent = parent

        self.lives_label = Label(self.parent.window, text=f"Lives:{self.game_logic.lives}",
                                 background=main_config.THEME_COLOR, fg=main_config.DEFAULT_FONT_COLOUR, width=10)
        # self.lives_label.config(self.stan_config.gl)
        self.lives_label.grid(column=0, row=0)

        self.score_label = Label(self.parent.window, text=f"Score:{self.game_logic.score}",
                                 background=main_config.THEME_COLOR, fg=main_config.DEFAULT_FONT_COLOUR, width=10)
        # self.score_label.config(self.stan_config.gl)
        self.score_label.grid(column=1, row=0)

    def give_feedback(self, players_choice):
        print("!!!This is the player's choice!:", players_choice)

        a = players_choice.split('-')

        if a[1] == "correct":
            if a[0] == 'option_1':
                self.game_display.border_1.config(background="green", bd=10)
            else:
                self.game_display.border_2.config(background="green", bd=10)

            sound_feedback(main_config.CORRECT_SOUND)

        elif a[1] == "incorrect":
            if a[0] == 'option_1':
                self.game_display.border_1.config(background="red", bd=10)
            else:
                self.game_display.border_2.config(background="red", bd=10)

            sound_feedback(main_config.INCORRECT_SOUND)

        self.score_label.config(text=f"Score:{self.game_logic.score}")
        self.lives_label.config(text=f"Lives:{self.game_logic.lives}")