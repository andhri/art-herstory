from tkinter import *
from game_logic_v3 import ArtGame
from display import DisplayConfig
import main_config
from parent_interface import Parent
from add_info_popup import OpenPopUp


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
        index1 = self.game_logic.database[option_1]

        art_title1 = index1["title"]
        add_info2 = f"{index1['artistDisplayName']}"
        print(f' additional info1:', self.game_logic.database[option_1]["artistDisplayName"])

        self.name_art_1.config(text=self.game_logic.replace_title_digits(art_title1))

        self.art_info.label2.config(text=f"{art_title1}",
                                    wraplength=200, justify='center', font='Helvetica 16 bold')
        self.art_info.label4.config(text=f"{add_info2}", wraplength=300, justify='center', font='Helvetica 16 bold')

        return option_1
        # return option_1, art_title1, add_info1

    def display_option_2(self):
        option_2 = self.game_logic.get_portrait_by_index('right')
        print(f" Art Details 2: {self.game_logic.database[option_2]}")
        index2 = self.game_logic.database[option_2]

        art_title2 = index2["title"]
        add_info2 = f"{index2['artistDisplayName']}"
        print(f' additional info2:', self.game_logic.database[option_2]["artistDisplayName"])

        self.name_art_2.config(text=self.game_logic.replace_title_digits(art_title2))

        self.art_info.label2.config(text=f"{art_title2}",
                                    wraplength=300, justify='center', font='Helvetica 16 bold')
        self.art_info.label4.config(text=f"{add_info2}", wraplength=300, justify='center', font='Helvetica 16 bold')

        return option_2
        # return option_2, art_title2, add_info2

    # def add_info_by_option(self):
    #     option_1 = self.game_logic.database[self.display_option_1()]
    #     option_2 = self.game_logic.database[self.display_option_2()]
    #
    #     art_title1 = option_1["title"]
    #     art_title1 = self.game_logic.replace_title_digits(art_title1)
    #     artist_name1 = option_1["artistDisplayName"]
    #     # country1 = option_1["country"]
    #     # culture1 = option_1["culture"]
    #
    #     art_title2 = option_1["title"]
    #     art_title2 = self.game_logic.replace_title_digits(art_title2)
    #     artist_name2 = option_2["artistDisplayName"]
    #     # country2 = option_2["country"]
    #     # culture2 = option_2["culture"]
    #
    #     if self.display_option_1():
    #         # self.art_info.add_info = f"{art_title1}", f"{artist_name1}, {country1}, {culture1}"
    #         self.art_info.add_info = f"{art_title1}", f"{artist_name1}"
    #
    #     elif self.display_option_2():
    #         # self.art_info.add_info = f"{art_title2}", f"{artist_name2}, {country2}, {culture2}"
    #         self.art_info.add_info = f"{art_title2}", f"{artist_name2}"
    #
    #     return self.art_info.add_info

    # def open_popup1(self):
    #     print('pop-up for image 1')
    #     OpenPopUp(self.parent)
    #     # self.art_info.label2.configure(text=self.display_option_1()[1], wraplength=300)
    #     # self.art_info.label4.config(text=self.display_option_2()[2], wraplength=300)
    #     # self.name_art_2.config(state="disabled")
    #
    #     # self.art_info.info_pop.deiconify()
    #     # print(self.add_info_by_option())
    #     # title = self.add_info_by_option()[0]
    #     # extra = self.add_info_by_option()[1::]
    #
    #     # OpenPopUp(self.parent, self.display_option_1())
    #     # OpenPopUp(self.parent, title, extra)
    #
    # def open_popup2(self):
    #     print('pop-up for image 2')
    #     OpenPopUp(self.parent)
    #     # self.art_info.label2.configure(text=self.display_option_2()[1], wraplength=300)
    #     # self.art_info.label4.config(text=self.display_option_2()[2], wraplength=300)
    #     # self.name_art_1.config(state="disabled")




