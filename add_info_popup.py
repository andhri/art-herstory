from tkinter import *
import main_config
from parent_interface import Parent


class OpenPopUp:
    """ Initialises the popup window that holds all of the additional information widgets """
    def __init__(self, parent: Parent, art_title=None, add_info=None):
        self.parent = parent
        self.info_pop = Toplevel()
        self.info_pop.geometry("400x410")
        self.info_pop.title("Additional Info")
        self.info_pop.iconbitmap("CFG_logo.ico")
        self.info_pop.lift()
        self.info_pop.config(bg=main_config.THEME_COLOR)
        self.info_pop.transient(self.parent.window)
        self.info_pop.grab_set()

        self.add_info = add_info
        self.art_title = art_title

        self.label1 = Label(self.info_pop, text="See more information on the artwork titled:", font=main_config.bf,
                            fg=main_config.TEXT_COLOUR, bg=main_config.THEME_COLOR, padx=50, pady=10)
        self.label1.grid(column=1, row=1)

        self.label2 = Label(self.info_pop, text=f"'{art_title}'", font=main_config.bf,
                            fg=main_config.DEFAULT_FONT_COLOUR, bg=main_config.THEME_COLOR, padx=50, pady=10,
                            wraplength=300)
        self.label2.grid(column=1, row=2)

        self.label3 = Label(self.info_pop, text=f"{'*' * 50}", font=main_config.bf,
                            fg=main_config.TEXT_COLOUR, bg=main_config.THEME_COLOR, padx=50, pady=10,
                            wraplength=300)
        self.label3.grid(column=1, row=3)

        self.label4 = Label(self.info_pop, text=f"{add_info}", font=main_config.pf,
                            fg=main_config.DEFAULT_FONT_COLOUR, bg=main_config.THEME_COLOR, padx=50, pady=20, wraplength=300)
        self.label4.grid(column=1, row=4)

        self.button = Button(self.info_pop, text="Close", highlightthickness=0, fg=main_config.DEFAULT_FONT_COLOUR,
                             activebackground=main_config.DEFAULT_FONT_COLOUR, background='white',
                             cursor=main_config.cur, highlightcolor=main_config.DEFAULT_FONT_COLOUR,
                             highlightbackground=main_config.THEME_COLOR, font=main_config.bf,
                             command=lambda: self.close_popup())
        self.button.grid(column=1, row=6)

    def close_popup(self):
        """ Method to close the popup window """
        self.info_pop.destroy()