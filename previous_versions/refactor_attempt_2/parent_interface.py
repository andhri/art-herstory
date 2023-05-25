from tkinter import *
import game_interface.main_config as main_config

# created this file just to separate main tkinter window so that could easily call in all other code files

class Parent:
    def __init__(self):
        self.window = Tk()
        self.window.title("ART Game")
        self.window.config(padx=20, pady=20, background=main_config.THEME_COLOR, height=600, width=500)

        self.canvas = Canvas(self.window)
        self.canvas.config(height=600, width=700, background=main_config.THEME_COLOR)
