from tkinter import *
import game_interface.main_config as mc
from game_interface.parent_interface import Parent


class OpenPopUp:
    """ Initialises the popup window that holds all of the additional information widgets """
    def __init__(self, parent: Parent, art_title=None, add_info=None):
        self.parent = parent
        self.info_pop = Toplevel()
        self.info_pop.geometry("400x410")
        self.info_pop.title("Additional Info")
        self.info_pop.iconbitmap(mc.logo)
        self.info_pop.lift()
        self.info_pop.config(bg=mc.THEME_COLOR)
        self.info_pop.transient(self.parent.window)
        self.info_pop.grab_set()

        self.add_info = add_info
        self.art_title = art_title

        self.label1 = Label(self.info_pop, text="See more information on the artwork titled:", font=mc.bf,
                            fg=mc.TEXT_COLOUR, bg=mc.THEME_COLOR, padx=50, pady=10)
        self.label1.grid(column=1, row=1)

        self.label2 = Label(self.info_pop, text=f"'{art_title}'", font=mc.bf,
                            fg=mc.DEFAULT_FONT_COLOUR, bg=mc.THEME_COLOR, padx=50, pady=10,
                            wraplength=300)
        self.label2.grid(column=1, row=2)

        self.label3 = Label(self.info_pop, text=f"{'*' * 50}", font=mc.bf,
                            fg=mc.TEXT_COLOUR, bg=mc.THEME_COLOR, padx=50, pady=10,
                            wraplength=300)
        self.label3.grid(column=1, row=3)

        self.label4 = Label(self.info_pop, text=f"{add_info}", font=mc.pf,
                            fg=mc.DEFAULT_FONT_COLOUR, bg=mc.THEME_COLOR, padx=50, pady=20, wraplength=300)
        self.label4.grid(column=1, row=4)

        self.button = Button(self.info_pop, text="Close", highlightthickness=0, fg=mc.DEFAULT_FONT_COLOUR,
                             activebackground=mc.DEFAULT_FONT_COLOUR, background='white',
                             cursor=mc.cur, highlightcolor=mc.DEFAULT_FONT_COLOUR,
                             highlightbackground=mc.THEME_COLOR, font=mc.bf,
                             command=lambda: self.close_popup())
        self.button.grid(column=1, row=6)

    def close_popup(self):
        """ Method to close the popup window """
        self.info_pop.destroy()