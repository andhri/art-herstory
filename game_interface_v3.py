from tkinter import *
from game_logic_v3 import ArtGame
from game_options import ArtOptions
from game_answers import GameAnswers
from display import DisplayConfig
from PIL import ImageTk, Image
import requests
from io import BytesIO

import main_config

THEME_COLOR = "#EAF6E8"

class GameInterface:
    def __init__(self, art_game: ArtGame, art_options: ArtOptions, answers: GameAnswers, game_display: DisplayConfig):
        self.game_logic = art_game
        self.art_options = art_options
        self.answers = answers
        # self.stan_config = main_config
        self.game_display = game_display
        self.window = Tk()
        self.window.title("ART Game")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)
        # the code above may be removed and merged with Kristina's code for main interface???

        self.canvas = Canvas()
        self.canvas.config(height=600, width=500, background=THEME_COLOR)

        self.title = Label(text="Which one came first?")
        self.title.config(background=THEME_COLOR, width=30, highlightthickness=0, padx=20, pady=20, font=("Helvetica", 40, "bold"))
        self.title.grid(column=0, row=1, columnspan=2)

        self.add_info_1 = None
        self.add_info_2 = None

        self.generate_options()

        self.window.mainloop()

        self.window.after(1000, self.generate_options)

    def generate_options(self):
        if self.game_logic.still_has_lives():
            self.art_options.display_option_1()
            self.art_options.display_option_2()
        else:
            print("You're Out of Lives!!")
            self.game_display.display_art_1.config(state="disabled")
            self.game_display.display_art_2.config(state="disabled")

    def option_1_answer(self):
        a1 = self.answers.give_feedback(self.game_logic.check_players_choice("option_1"))

        img1 = self.game_display.option_image(self.art_options.display_option_1().option_1)
        self.game_display.display_art_1.config(image=img1, command=a1)
        self.game_display.display_art_1.image = img1

    def option_2_answer(self):
        a2 = self.answers.give_feedback(self.game_logic.check_players_choice("option_2"))

        img2 = self.game_display.option_image(self.art_options.display_option_2().option_2)
        self.game_display.display_art_1.config(image=img2, command=a2)
        self.game_display.display_art_1.image = img2



    # still working on this.....
    # def open_popup(self):
    #     InfoPopup().add_info_by_option()

    # def add_info_by_option(self):
    #     # self.add_info_1 = self.option_1["artistDisplayName", "country", "culture"]
    #     # self.add_info_2 = self.option_2["artistDisplayName", "country", "culture"]
    #
    #     # this function isn't ready yet and still working on it....
    #     if self.generate_options() = 'option_1':
    #         self.add_info_1 = self.generate_options().option_1["artistDisplayName", "country", "culture"]
    #         print(self.add_info_1)
    #
    #     elif self.generate_options().option_2:
    #         self.add_info_2 = self.generate_options().option_2["artistDisplayName", "country", "culture"]
    #         print(self.add_info_2)
    #
    # def close_popup(self):
    #     self.destroy()










