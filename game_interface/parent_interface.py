from tkinter import *
from tkinter.messagebox import showinfo
import game_interface.main_config as mc


# main interface window
class Parent:
    """Initialises the main window"""
    def __init__(self):
        showinfo(title="Welcome!", message=mc.welcome_intro)
        self.window = Tk()

        self.window.title("Art HerStory")
        self.window.config(height=600, width=500, padx=20, pady=20, background=mc.THEME_COLOR)

        self.window.iconbitmap(mc.logo)

        self.canvas = Canvas(self.window)
        self.canvas.config(height=600, width=700, background=mc.THEME_COLOR)

        self.title = Label(self.window, text="Which was made first?", background=mc.THEME_COLOR, width=30,
                           highlightthickness=0, padx=20, pady=20, font=mc.font_title,
                           fg=mc.DEFAULT_FONT_COLOUR)
        self.title.grid(column=0, row=1, columnspan=2)

        self.instructions_button = Button(self.window, text="  i  ", font=mc.i_font, fg=mc.DEFAULT_FONT_COLOUR,
                                          activebackground=mc.DEFAULT_FONT_COLOUR, background='white',
                                          relief=RIDGE, cursor=mc.cur, highlightcolor=mc.DEFAULT_FONT_COLOUR,
                                          highlightbackground=mc.THEME_COLOR, command=self.show_instructions)
        self.instructions_button.grid(column=0, row=0, columnspan=2)

    def show_instructions(self):
        """Method to display instructions which helps the player """
        global pop
        pop = Toplevel(self.window, bg=mc.THEME_COLOR)
        pop.title("Game Rules")
        pop_label = Label(pop, text=mc.game_instructions, bg="orange")
        pop_label.pack()