from tkinter import *
from game_logic_try import ArtGame
from PIL import ImageTk, Image
import requests
from io import BytesIO
import pygame

THEME_COLOR = "#EAF6E8"
CORRECT_SOUND = "correct-6033.mp3"
INCORRECT_SOUND = "incorrect-buzzer-sound-147336.mp3"


class GameInterface:
    def __init__(self, art_game: ArtGame):
        self.game = art_game
        self.window = Tk()
        self.window.title("ART Game")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas()
        self.canvas.config(height=600, width=500, bg=THEME_COLOR)

        self.lives_label = Label(text=f"Lives:{self.game.lives}", bg=THEME_COLOR, width=10, highlightthickness=0)
        self.lives_label.grid(column=0, row=0)

        self.score_label = Label(text=f"Score:{self.game.score}", bg=THEME_COLOR, width=10, highlightthickness=0)
        self.score_label.grid(column=1, row=0)

        self.title = Label(text="Which one came first?", bg=THEME_COLOR, width=30, highlightthickness=0, padx=20,
                           pady=20, font=("Helvetica", 40, "bold"))
        self.title.grid(column=0, row=1, columnspan=2)

        # these two will have to changed into buttons for the message box to pop
        self.name_art_1 = Label(text="option_1.art_name", width=20, bg=THEME_COLOR, highlightthickness=0)
        self.name_art_1.grid(column=0, row=2)

        self.name_art_2 = Label(text="option_2.art_name", width=20, bg=THEME_COLOR, highlightthickness=0)
        self.name_art_2.grid(column=1, row=2)

        self.border_1 = LabelFrame(background=THEME_COLOR, bd=10)
        self.border_1.grid(column=0, row=3, padx=20, pady=20)

        self.display_art_1 = Button(self.border_1, text="Option 1", highlightthickness=0)
        self.display_art_1.grid(column=0, row=3)

        self.border_2 = LabelFrame(background=THEME_COLOR, bd=10)
        self.border_2.grid(column=1, row=3, padx=20, pady=20)

        self.display_art_2 = Button(self.border_2, text="Option 1", highlightthickness=0)
        self.display_art_2.grid(column=1, row=3)

        self.generate_options()

        self.window.mainloop()

    def option_1_answer(self):
        self.give_feedback(self.game.check_players_choice("option_1"))

    def option_2_answer(self):
        self.give_feedback(self.game.check_players_choice("option_2"))

    def generate_options(self):
        self.border_1.config(background=THEME_COLOR, bd=10)
        self.border_2.config(background=THEME_COLOR, bd=10)

        if self.game.still_has_lives():
            option_1 = self.game.get_portrait_by_index('left')
            print(self.game.database[option_1])
            option_2 = self.game.get_portrait_by_index('right')
            print(self.game.database[option_2])

            url1 = self.game.database[option_1]["primaryImage"]
            u = requests.get(url1)
            img1 = Image.open(BytesIO(u.content))
            img1 = img1.resize((400, 550), Image.LANCZOS)
            img1 = ImageTk.PhotoImage(img1)

            self.name_art_1.config(text=self.game.database[option_1]["objectID"])
            self.name_art_2.config(text=self.game.database[option_2]["objectID"])

            self.display_art_1.config(image=img1, command=self.option_1_answer)
            self.display_art_1.image = img1

            url2 = self.game.database[option_2]["primaryImage"]
            u = requests.get(url2)
            img2 = Image.open(BytesIO(u.content))
            img2 = img2.resize((400, 550), Image.LANCZOS)
            img2 = ImageTk.PhotoImage(img2)

            self.display_art_2.config(image=img2, command=self.option_2_answer)
            self.display_art_2.image = img2
        else:
            print("you lost")
            self.display_art_1.config(state="disabled")
            self.display_art_2.config(state="disabled")
            # here will probably go the code to generate the next frame to save the score

    def sound_feedback(self, sound):
        pygame.mixer.init()
        pygame.mixer.music.load(sound)
        pygame.mixer.music.play(loops=0)

    def give_feedback(self, players_choice):
        print("!!!this is players choice!", players_choice)

        a = players_choice.split('-')

        if a[1] == "correct":
            if a[0] == 'option_1':
                self.border_1.config(background="green", bd=10)
            else:
                self.border_2.config(background="green", bd=10)

            # self.correct_answer_sound()
            self.sound_feedback(CORRECT_SOUND)
        elif a[1] == "incorrect":
            if a[0] == 'option_1':
                self.border_1.config(background="red", bd=10)
            else:
                self.border_2.config(background="red", bd=10)

            self.sound_feedback(INCORRECT_SOUND)

        self.score_label.config(text=f"Score:{self.game.score}")
        self.lives_label.config(text=f"Lives:{self.game.lives}")
        self.window.after(1000, self.generate_options)
