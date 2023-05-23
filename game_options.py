from tkinter import *
from game_logic_v3 import ArtGame
from display import DisplayConfig
import main_config
from parent_interface import Parent
from add_info_popup import OpenPopUp
from met_data import load_data


class ArtOptions:
    def __init__(self, parent: Parent, game_logic: ArtGame, game_display: DisplayConfig, art_info: OpenPopUp):
        self.game_logic = game_logic
        self.game_display = game_display
        self.parent = parent
        self.art_info = art_info

        self.name_art_1 = Button(self.parent.window, text="option_1.art_name", width=30, bg=main_config.THEME_COLOR)
        self.name_art_1.bind('<Configure>', lambda e: self.name_art_1.config(wraplength=self.name_art_1.winfo_width()))
        self.name_art_1.grid(column=0, row=2)

        self.name_art_2 = Button(self.parent.window, text="option_2.art_name", width=30, bg=main_config.THEME_COLOR)
        self.name_art_2.bind('<Configure>', lambda e: self.name_art_2.config(wraplength=self.name_art_2.winfo_width()))
        self.name_art_2.grid(column=1, row=2)

    def display_option_1(self):
        option_1 = self.game_logic.get_portrait_by_index('left')
        print(f" Art Details 1: {self.game_logic.database[option_1]}")
        art1 = self.game_logic.database[option_1]

        art_title1 = art1["title"]
        add_info1 = f"{art1['artistDisplayName']}"
        print(f' additional info1:', self.game_logic.database[option_1]["artistDisplayName"])

        self.name_art_1.config(text=self.game_logic.replace_title_digits(art_title1), command=lambda: open_popup1())

        def open_popup1():
            print('pop-up for image 1')
            OpenPopUp(self.parent, self.game_logic.replace_title_digits(art_title1), add_info1)

        return option_1

    def display_option_2(self):
        option_2 = self.game_logic.get_portrait_by_index('right')
        print(f" Art Details 2: {self.game_logic.database[option_2]}")
        art2 = self.game_logic.database[option_2]

        art_title2 = art2["title"]
        add_info2 = f"{art2['artistDisplayName']}"
        print(f' additional info2:', self.game_logic.database[option_2]["artistDisplayName"])

        self.name_art_2.config(text=self.game_logic.replace_title_digits(art_title2), command=lambda: open_popup2())

        def open_popup2():
            print('pop-up for image 2')
            OpenPopUp(self.parent, self.game_logic.replace_title_digits(art_title2), add_info2)

        return option_2



