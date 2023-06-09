from tkinter import *
import pygame
from game_logic.game_logic import ArtGame
from game_interface.game_options import ArtOptions
from game_interface.display import DisplayConfig
import game_interface.main_config as mc
from game_interface.parent_interface import Parent


def sound_feedback(sound):
    """Function which handles the sound based on an mp3file """
    pygame.mixer.init()            # using pygame library to add sound effects
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play(loops=0)


class GameAnswers:
    """Intilises the lives and the score attributes as Label widgets """
    def __init__(self, parent: Parent, game_logic: ArtGame, display: DisplayConfig):
        self.art_options = ArtOptions
        self.answers = GameAnswers
        self.game_logic = game_logic
        self.game_display = display
        self.parent = parent

        self.lives_label = Label(self.parent.window, text=f"Lives: {self.game_logic.lives}",
                                 background=mc.THEME_COLOR, fg=mc.TEXT_COLOUR,
                                 width=10, font=mc.font_body)
        self.lives_label.grid(column=0, row=0)

        self.score_label = Label(self.parent.window, text=f"Score: {self.game_logic.score}",
                                 background=mc.THEME_COLOR, fg=mc.TEXT_COLOUR,
                                 width=10, font=mc.font_body)
        self.score_label.grid(column=1, row=0)


    def give_feedback(self, players_choice):
        """Method to provide the user with visual and audio feedback based on their answers """
        a = players_choice.split('-')

        if a[1] == "correct":
            if a[0] == 'option_1':
                self.game_display.border_1.config(background="green", bd=10)
            else:
                self.game_display.border_2.config(background="green", bd=10)

            sound_feedback(mc.CORRECT_SOUND)

        elif a[1] == "incorrect":
            if a[0] == 'option_1':
                self.game_display.border_1.config(background="red", bd=10)
            else:
                self.game_display.border_2.config(background="red", bd=10)

            sound_feedback(mc.INCORRECT_SOUND)

        self.score_label.config(text=f"Score: {self.game_logic.score}")
        self.lives_label.config(text=f"Lives: {self.game_logic.lives}")