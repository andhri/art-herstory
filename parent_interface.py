from tkinter import *
from tkinter.messagebox import showinfo
import main_config

# created this file just to separate main tkinter window so that could easily call in all other code files

""" Initialises the main GUI interface """
class Parent:
    def __init__(self):
        showinfo(title="Welcome!", message=main_config.welcome_intro)
        self.window = Tk()
        # self.window.geometry("1000x800")
        self.window.title("Art HerStory")
        self.window.config(height=600, width=500, padx=20, pady=20, background=main_config.THEME_COLOR)

        self.window.iconbitmap("Black-Code-First-Girls-Logo-Transparent-700x700.ico")

        self.canvas = Canvas(self.window)
        self.canvas.config(height=600, width=700, background=main_config.THEME_COLOR)

        self.title = Label(self.window, text="Which was made first?", background=main_config.THEME_COLOR, width=30,
                           highlightthickness=0, padx=20, pady=20, font=main_config.font_title,
                           fg=main_config.DEFAULT_FONT_COLOUR)
        self.title.grid(column=0, row=1, columnspan=2)

        # i_image = (Image.open("i_icon.png"))
        # resized_image= i_image.resize((10,5), Image.LANCZOS)
        # new_image = PhotoImage(resized_image)
        # image = new_image
        self.instructions_button = Button(self.window, text="i", fg=main_config.DEFAULT_FONT_COLOUR,
                                          highlightbackground=main_config.THEME_COLOR, command=self.show_instructions)
        self.instructions_button.grid(column=1, row=1)

    """ Function to display instructions which helps the player """
    def show_instructions(self):
        global pop
        pop = Toplevel(self.window, bg=main_config.THEME_COLOR)
        pop.title("Game Rules")
        pop_label = Label(pop, text=main_config.game_instructions, bg="orange")
        pop_label.pack()