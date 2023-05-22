from tkinter import *
from game_logic_v3 import ArtGame
from PIL import ImageTk, Image
import requests
from io import BytesIO
from game_answers import GameAnswers
from display import DisplayConfig

THEME_COLOR = "#EAF6E8"


class ArtOptions:
    def __init__(self, game_logic: ArtGame, answers: GameAnswers, game_display: DisplayConfig):
        self.game_logic = game_logic
        self.answers = answers
        self.game_display = game_display

        # self.name_art_1 = Button(text="option_1.art_name", width=30, bg=THEME_COLOR, command=lambda: self.open_popup())
        # self.name_art_1.bind('<Configure>', lambda e: self.name_art_1.config(wraplength=self.name_art_1.winfo_width()))
        # self.name_art_1.grid(column=0, row=3)
        #
        # self.name_art_2 = Button(text="option_2.art_name", width=30, bg=THEME_COLOR, command=lambda: self.open_popup())
        # self.name_art_2.bind('<Configure>', lambda e: self.name_art_2.config(wraplength=self.name_art_2.winfo_width()))
        # self.name_art_2.grid(column=1, row=3)

        self.name_art_1 = Button(text="option_1.art_name", width=30, bg=THEME_COLOR)
        self.name_art_1.bind('<Configure>', lambda e: self.name_art_1.config(wraplength=self.name_art_1.winfo_width()))
        self.name_art_1.grid(column=0, row=3)

        self.name_art_2 = Button(text="option_2.art_name", width=30, bg=THEME_COLOR)
        self.name_art_2.bind('<Configure>', lambda e: self.name_art_2.config(wraplength=self.name_art_2.winfo_width()))
        self.name_art_2.grid(column=1, row=3)

        # # self.border_1 = LabelFrame(background=THEME_COLOR, bd=10)
        # # self.border_1.grid(column=0, row=2, padx=20, pady=20)
        #
        # self.display_art_1 = Button(self.answers.border_1, text="Option 1", highlightthickness=0)
        # self.display_art_1.grid(column=0, row=2)
        #
        # # self.border_2 = LabelFrame(background=THEME_COLOR, bd=10)
        # # self.border_2.grid(column=1, row=2, padx=20, pady=20)
        #
        # self.display_art_2 = Button(self.answers.border_2, text="Option 2", highlightthickness=0)
        # self.display_art_2.grid(column=1, row=2)

    # function checks if player still has lives - if so then displays option1 & option2;
    # if not, then switches frame to results page - where overall score is presented to player & they can save to lb
    # def generate_options(self):
    #     if self.game_logic.still_has_lives():
    #         self.display_option_1()
    #         self.display_option_2()
    #     else:
    #         print("You're Out of Lives!!")
    #         self.game_display.display_art_1.config(state="disabled")
    #         self.game_display.display_art_2.config(state="disabled")
            # here will probably go the code to generate the next frame to save the score

    def display_option_1(self):
        option_1 = self.game_logic.get_portrait_by_index('left')
        print(self.game_logic.database[option_1])

        art_title1 = self.game_logic.database[option_1]["title"]
        print(f' additional info1:', self.game_logic.database[option_1]["artistDisplayName"])

        self.name_art_1.config(text=self.game_logic.replace_title_digits(art_title1))

        # url1 = self.game_logic.database[option_1]["primaryImage"]
        # u = requests.get(url1)
        # img1 = Image.open(BytesIO(u.content))
        # img1 = img1.resize((400, 550), Image.LANCZOS)
        # img1 = ImageTk.PhotoImage(img1)

        # call to function in display file
        # img1 = self.game_display.option_image(option_1)

        # self.game_display.display_art_1.config(image=img1, command=self.answers.option_1_answer)
        # self.game_display.display_art_1.image = img1

        # return option_1

    def display_option_2(self):
        option_2 = self.game_logic.get_portrait_by_index('right')
        print(self.game_logic.database[option_2])

        art_title2 = self.game_logic.database[option_2]["title"]
        print(f' additional info2:', self.game_logic.database[option_2]["artistDisplayName"])

        self.name_art_2.config(text=self.game_logic.replace_title_digits(art_title2))

        # url2 = self.game_logic.database[option_2]["primaryImage"]
        # u = requests.get(url2)
        # img2 = Image.open(BytesIO(u.content))
        # img2 = img2.resize((400, 550), Image.LANCZOS)
        # img2 = ImageTk.PhotoImage(img2)

        # call to function in display file
        # img2 = self.game_display.option_image(option_2)

        # self.game_display.display_art_2.config(image=img2, command=self.answers.option_2_answer)
        # self.game_display.display_art_2.image = img2

        # return option_2
