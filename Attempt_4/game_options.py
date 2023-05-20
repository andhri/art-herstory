from tkinter import *
from game_logic_v4 import ArtGame
from display import DisplayConfig
import main_config
from parent_interface import Parent


class ArtOptions:
    def __init__(self, parent: Parent, game_logic: ArtGame, game_display: DisplayConfig):
        self.game_logic = game_logic
        # self.answers = answers
        self.game_display = game_display
        self.parent = parent

        self.name_art_1 = Button(self.parent.window, text="option_1.art_name", width=30, bg=main_config.THEME_COLOR)
        self.name_art_1.bind('<Configure>', lambda e: self.name_art_1.config(wraplength=self.name_art_1.winfo_width()))
        self.name_art_1.grid(column=0, row=3)

        self.name_art_2 = Button(self.parent.window, text="option_2.art_name", width=30, bg=main_config.THEME_COLOR)
        self.name_art_2.bind('<Configure>', lambda e: self.name_art_2.config(wraplength=self.name_art_2.winfo_width()))
        self.name_art_2.grid(column=1, row=3)

    def display_option_1(self):
        option_1 = self.game_logic.get_portrait_by_index('left')
        print("print option 1", self.game_logic.database[option_1])
        print("this is display_option 1", option_1)

        art_title1 = self.game_logic.database[option_1]["title"]
        print(f' additional info1:', self.game_logic.database[option_1]["artistDisplayName"])

        self.name_art_1.config(text=self.game_logic.replace_title_digits(art_title1))
        # self.name_art_1.config(text=art_title1)

        return option_1

    def display_option_2(self):
        option_2 = self.game_logic.get_portrait_by_index('right')
        print("print option 2", self.game_logic.database[option_2])
        print("this is display_option 2", option_2)

        art_title2 = self.game_logic.database[option_2]["title"]
        print(f' additional info2:', self.game_logic.database[option_2]["artistDisplayName"])

        self.name_art_2.config(text=self.game_logic.replace_title_digits(art_title2))
        # self.name_art_2.config(text=art_title2)
        return option_2