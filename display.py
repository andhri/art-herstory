from tkinter import *
from game_logic_v3 import ArtGame
import requests
from io import BytesIO
from PIL import ImageTk, Image

THEME_COLOR = "#EAF6E8"


class DisplayConfig:

    def __init__(self, game_logic: ArtGame):
        self.game_logic = game_logic

        self.border_1 = LabelFrame(background=THEME_COLOR, bd=10)
        self.border_1.grid(column=0, row=2, padx=20, pady=20)

        self.border_2 = LabelFrame(background=THEME_COLOR, bd=10)
        self.border_2.grid(column=1, row=2, padx=20, pady=20)

        self.display_art_1 = Button(self.border_1, text="Option 1", highlightthickness=0)
        self.display_art_1.grid(column=0, row=2)

        self.display_art_2 = Button(self.border_2, text="Option 2", highlightthickness=0)
        self.display_art_2.grid(column=1, row=2)

    def option_image(self, a):
        url = self.game_logic.database[a]["primaryImage"]
        u = requests.get(url)
        img = Image.open(BytesIO(u.content))
        img = img.resize((400, 550), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)

        return img
