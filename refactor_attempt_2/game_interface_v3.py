from tkinter import *
from game_logic_v3 import ArtGame
from game_options import ArtOptions
from game_answers import GameAnswers
from display import DisplayConfig
import main_config
from parent_interface import Parent


class GameInterface:
    def __init__(self, parent: Parent, art_game: ArtGame, art_options: ArtOptions,
                 answers: GameAnswers, game_display: DisplayConfig):
        self.game_logic = art_game
        self.art_options = art_options
        self.answers = answers
        # self.stan_config = main_config
        self.game_display = game_display

        self.parent = parent

        self.title = Label(self.parent.window, text="Which one came first?")
        self.title.config(background=main_config.THEME_COLOR, width=30, highlightthickness=0, padx=20, pady=20,
                          font=("Helvetica", 40, "bold"), fg=main_config.DEFAULT_FONT_COLOUR)
        self.title.grid(column=0, row=1, columnspan=2)

        # self.add_info_1 = None
        # self.add_info_2 = None

        self.generate_options()

        self.parent.window.mainloop()

    def generate_options(self):
        if self.game_logic.still_has_lives():
            self.art_options.display_option_1()

            img1 = self.game_display.option_image(self.art_options.display_option_1())
            self.game_display.display_art_1.config(image=img1, command=self.option_1_answer)
            self.game_display.display_art_1.image = img1

            self.art_options.display_option_2()

            img2 = self.game_display.option_image(self.art_options.display_option_2())

            self.game_display.display_art_2.config(image=img2, command=self.option_2_answer)
            self.game_display.display_art_2.image = img2

        else:
            print("You're Out of Lives!!")
            self.game_display.display_art_1.config(state="disabled")
            self.game_display.display_art_2.config(state="disabled")

    def option_1_answer(self):
        self.answers.give_feedback(self.game_logic.check_players_choice("option_1"))
        self.parent.window.after(1000, self.generate_options)

    def option_2_answer(self):
        self.answers.give_feedback(self.game_logic.check_players_choice("option_2"))
        self.parent.window.after(1000, self.generate_options)

    # still working on this.....
    # def open_popup(self):
    #     InfoPopup().add_info_by_option()
    #
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










