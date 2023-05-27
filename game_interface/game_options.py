import logging
from tkinter import *
from game_logic.game_logic import ArtGame
from game_interface.display import DisplayConfig
import game_interface.main_config as mc
from game_interface.parent_interface import Parent
from game_interface.add_info_popup import OpenPopUp

# log for options that user engaged with, they can revisit the artworks they looked at
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter(":%(asctime)s:%(name)s:%(message)s")

file_handler =  logging.FileHandler('logs/options.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


class ArtOptions:
    """Initialises the widgets that hold the additional information on each picture"""
    def __init__(self, parent: Parent, game_logic: ArtGame, game_display: DisplayConfig):
        self.game_logic = game_logic
        self.game_display = game_display
        self.parent = parent

        self.name_art_1 = Button(self.parent.window, text="option_1.art_name", width=30, bg=mc.THEME_COLOR, cursor=mc.cur,
                                 highlightbackground=mc.THEME_COLOR, font=mc.bf, fg=mc.TEXT_COLOUR)
        self.name_art_1.bind('<Configure>', lambda e: self.name_art_1.config(wraplength=self.name_art_1.winfo_width()))
        self.name_art_1.grid(column=0, row=3)

        self.name_art_2 = Button(self.parent.window, text="option_2.art_name", width=30, bg=mc.THEME_COLOR, cursor=mc.cur,
                                 highlightbackground=mc.THEME_COLOR, font=mc.bf, fg=mc.TEXT_COLOUR)
        self.name_art_2.bind('<Configure>', lambda e: self.name_art_2.config(wraplength=self.name_art_2.winfo_width()))
        self.name_art_2.grid(column=1, row=3)

    @staticmethod
    def empty_addinfo_var(a):
        """Checks for blacks and replaces them with '-' """
        if a == "" or a is None:
            return 'unknown'
        else:
            return a
    
    def display_option_1(self):
        """Method to get the data associated with the index generated for option 1 and display it in the pop up """
        option_1 = self.game_logic.get_portrait_by_index('left')
        logger.info(" Option 1 artist's name: %s", self.game_logic.database[option_1]["artistDisplayName"])
        logger.info(" Option 1 title: %s", self.game_logic.database[option_1]["title"])
        logger.info(" Option 2 image: %s", self.game_logic.database[option_1]["primaryImage"])
        logger.info(" Option 2 WikiQID: %s", self.game_logic.database[option_1]["artistWikidata_URL"])

        art1 = self.game_logic.database[option_1]

        art_title1 = art1["title"]
        add_info1 = f" Artist Name: '{art1['artistDisplayName']}'," \
                    f"\nCulture: '{self.empty_addinfo_var(art1['culture'])}'," \
                    f"\nCountry: '{self.empty_addinfo_var(art1['country'])}'"

        self.name_art_1.config(text=self.game_logic.replace_title_digits(art_title1), command=lambda: open_popup1())

        def open_popup1():
            OpenPopUp(self.parent, self.game_logic.replace_title_digits(art_title1), add_info1)

        return option_1

    def display_option_2(self):
        """Method to get the data associated with the index generated for option 2 and display it in the pop up """
        option_2 = self.game_logic.get_portrait_by_index('right')
        logger.info(" Option 2 artist's name: %s", self.game_logic.database[option_2]["artistDisplayName"])
        logger.info(" Option 2 title: %s", self.game_logic.database[option_2]["title"])
        logger.info(" Option 2 image: %s", self.game_logic.database[option_2]["primaryImage"])
        logger.info(" Option 2 WikiQID: %s", self.game_logic.database[option_2]["artistWikidata_URL"])
        art2 = self.game_logic.database[option_2]

        art_title2 = art2["title"]
        add_info2 = f" Artist Name: '{art2['artistDisplayName']}'," \
                    f"\nCulture: '{self.empty_addinfo_var(art2['culture'])}'," \
                    f"\nCountry: '{self.empty_addinfo_var(art2['country'])}'"

        self.name_art_2.config(text=self.game_logic.replace_title_digits(art_title2), command=lambda: open_popup2())

        def open_popup2():
            OpenPopUp(self.parent, self.game_logic.replace_title_digits(art_title2), add_info2)

        return option_2
