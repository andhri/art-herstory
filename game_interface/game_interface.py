from game_logic.game_logic import ArtGame
from game_interface.score import SaveGameScore
from game_interface.game_options import ArtOptions
from game_interface.game_answers import GameAnswers
from game_interface.display import DisplayConfig
from game_interface.parent_interface import Parent
import game_interface.main_config as main_config


class GameInterface:
    """Class for game elements options"""
    def __init__(self, parent: Parent, art_game: ArtGame, art_options: ArtOptions,
                 answers: GameAnswers, game_display: DisplayConfig):
        self.game_logic = art_game
        self.art_options = art_options
        self.answers = answers
        self.game_display = game_display
        self.parent = parent
        self.generate_options()
        self.parent.window.mainloop()

    def generate_options(self):
        """ Generates 2 random options while the player still has lives; otherwise it triggers the next window """
        self.game_display.border_1.config(background=main_config.THEME_COLOR, bd=10)
        self.game_display.border_2.config(background=main_config.THEME_COLOR, bd=10)

        if self.game_logic.still_has_lives():

            img1 = self.game_display.option_image(self.art_options.display_option_1())
            self.game_display.display_art_1.config(image=img1, command=self.option_1_answer)
            self.game_display.display_art_1.image = img1

            img2 = self.game_display.option_image(self.art_options.display_option_2())
            self.game_display.display_art_2.config(image=img2, command=self.option_2_answer)
            self.game_display.display_art_2.image = img2

        else:
            print("You're Out of Lives!!")
            self.game_display.display_art_1.config(state="disabled")
            self.game_display.display_art_2.config(state="disabled")
            self.parent.window.destroy()
            self.parent.window.after(1000, SaveGameScore(self.game_logic))

    def option_1_answer(self):
        """ Passes user's choice, compares it with the correct answer and then provides feedback to the user; triggers the next options """
        self.answers.give_feedback(self.game_logic.check_players_choice("option_1"))
        self.parent.window.after(1000, self.generate_options)

    def option_2_answer(self):
        """ Passes user's choice, compares it with the correct answer and then provides feedback to the user; triggers the next options """
        self.answers.give_feedback(self.game_logic.check_players_choice("option_2"))
        self.parent.window.after(1000, self.generate_options)
