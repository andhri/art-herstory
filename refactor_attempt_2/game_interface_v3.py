from tkinter import *
from game_logic_v3 import ArtGame
from game_options import ArtOptions
from game_answers import GameAnswers
from display import DisplayConfig
import main_config
from parent_interface import Parent
from add_info_popup import OpenPopUp


class GameInterface:
    def __init__(self, parent: Parent, art_game: ArtGame, art_options: ArtOptions,
                 answers: GameAnswers, game_display: DisplayConfig, art_info: OpenPopUp):
        self.game_logic = art_game
        self.art_options = art_options
        self.answers = answers
        # self.stan_config = main_config
        self.game_display = game_display
        self.art_info = art_info

        self.parent = parent

        self.title = Label(self.parent.window, text="Which one came first?")
        self.title.config(background=main_config.THEME_COLOR, width=30, highlightthickness=0, padx=20, pady=20,
                          font=("Helvetica", 40, "bold"), fg=main_config.DEFAULT_FONT_COLOUR)
        self.title.grid(column=0, row=1, columnspan=2)

        self.generate_options()

        self.parent.window.mainloop()

    def open_popup1(self):
        print('pop-up for image 1')
        OpenPopUp(self.parent)
        # OpenPopUp(self.parent, title1, info1)

    def open_popup2(self):
        print('pop-up for image 2')
        OpenPopUp(self.parent)
        # OpenPopUp(self.parent, title2, info2)

    def generate_options(self):
        self.game_display.border_1.config(background=main_config.THEME_COLOR, bd=10)
        self.game_display.border_2.config(background=main_config.THEME_COLOR, bd=10)

        if self.game_logic.still_has_lives():

            img1 = self.game_display.option_image(self.art_options.display_option_1())
            self.game_display.display_art_1.config(image=img1, command=self.option_1_answer)
            self.game_display.display_art_1.image = img1

            # self.art_info.label2.config(text=self.art_options.display_option_1()[1], wraplength=300)
            # self.art_info.label4.config(text=self.art_options.display_option_1()[2], wraplength=300)
            self.art_options.name_art_1.config(command=lambda: self.open_popup1())

            img2 = self.game_display.option_image(self.art_options.display_option_2())
            self.game_display.display_art_2.config(image=img2, command=self.option_2_answer)
            self.game_display.display_art_2.image = img2

            # self.art_info.label2.config(text=self.art_options.display_option_2()[1], wraplength=300)
            # self.art_info.label4.config(text=self.art_options.display_option_2()[2], wraplength=300)
            self.art_options.name_art_2.config(command=lambda: self.open_popup2())

        else:
            print("You're Out of Lives!!")
            self.game_display.display_art_1.config(state="disabled")
            self.game_display.display_art_2.config(state="disabled")

            self.title.config(text="You're Out Of Lives!", fg="red")

    def option_1_answer(self):
        self.answers.give_feedback(self.game_logic.check_players_choice("option_1"))
        self.parent.window.after(1000, self.generate_options)

    def option_2_answer(self):
        self.answers.give_feedback(self.game_logic.check_players_choice("option_2"))
        self.parent.window.after(1000, self.generate_options)












