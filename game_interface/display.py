from tkinter import *
from game_logic.game_logic import ArtGame
import requests
from io import BytesIO
from PIL import ImageTk, Image
import game_interface.main_config as mc
from game_interface.parent_interface import Parent


class DisplayConfig:
    """Initiates the widgets (LabelFrame & Button) which are a core part of the game"""
    def __init__(self, parent: Parent, game_logic: ArtGame):
        self.game_logic = game_logic
        self.parent = parent

        self.border_1 = LabelFrame(self.parent.window, background=mc.THEME_COLOR, bd=10)
        self.border_1.grid(column=0, row=2, padx=20, pady=20)

        self.border_2 = LabelFrame(self.parent.window, background=mc.THEME_COLOR, bd=10)
        self.border_2.grid(column=1, row=2, padx=20, pady=20)

        self.display_art_1 = Button(self.border_1, text="Option 1", cursor=mc.cur, highlightthickness=0)
        self.display_art_1.grid(column=0, row=2)

        self.display_art_2 = Button(self.border_2, text="Option 2", cursor=mc.cur, highlightthickness=0)
        self.display_art_2.grid(column=1, row=2)

    def option_image(self, a):
        """Method to create an image from an URL and then resize it to fit into the screen."""
        url = self.game_logic.database[a]["primaryImage"]
        u = requests.get(url)
        img = Image.open(BytesIO(u.content))
        img = img.resize((400, 550), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)

        return img
