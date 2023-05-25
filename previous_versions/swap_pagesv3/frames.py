import tkinter as tk
from tkinter import *
from game_logic_try import ArtGame
LARGEFONT =("Verdana", 16)
THEME_COLOR = "#ECDFEC"

class StartPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		text = Label(self, text ='Welcome to "ArtGame"', font = LARGEFONT)
		text.pack(padx = 10, pady = 10, anchor=tk.N)

		instructions = Label(self, text='Instructions')
		instructions.pack(fill='x')

		button1 = Button(self, text ="Play Game",command = lambda : controller.show_frame(GamePage))
		button1.pack(padx = 10, pady = 10)

		button2 = Button(self, text ="Leaderboard",
		command = controller.show_leaderboard)
		button2.pack(padx = 10, pady = 10)
 
class GamePage(tk.Frame):
	
	def __init__(self, parent, art_game = ArtGame):
		tk.Frame.__init__(self, parent)

		self.game = art_game
		self.lives_label = Label(text=f"Lives:{self.game.lives}", background=THEME_COLOR, width=10)
		self.lives_label.pack(padx=10, pady=10, anchor=tk.NW)

		self.score_label = Label(text=f"Score:{self.game.score}", background=THEME_COLOR, width=10)
		self.score_label.pack(padx=10, pady=10, anchor=tk.NE)

		self.title = Label(text="Which one came first?", background=THEME_COLOR, width=30, padx=20,pady=20, font=("Helvetica", 40, "bold"))
		self.title.pack(anchor=tk.N)

		self.name_art_1 = Button(text="option_1.art_name", width=40, background=THEME_COLOR)
		self.name_art_1.bind('<Configure>', lambda e: self.name_art_2.config(wraplength=self.name_art_2.winfo_width()))
		self.name_art_1.pack(padx=10, pady=10, anchor=tk.W)

		self.name_art_2 = Button(text="option_2.art_name", width=40, background=THEME_COLOR)
		self.name_art_2.bind('<Configure>', lambda e: self.name_art_2.config(wraplength=self.name_art_2.winfo_width()))
		self.name_art_2.pack(padx=10, pady=10, anchor=tk.E)

	# -----------------------------------------------------------------------------------------------

		self.border_1 = LabelFrame(background=THEME_COLOR, bd=10)
		self.border_1.pack(padx=20, pady=20)

		self.display_art_1 = Button(self.border_1, text="Option 1")
		self.display_art_1.pack(anchor=tk.W)

		self.border_2 = LabelFrame(background=THEME_COLOR, bd=10)
		self.border_2.pack(padx=20, pady=20)

		self.display_art_2 = Button(self.border_2, text="Option 2")
		self.display_art_2.pack(anchor=tk.E)


class ResultPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		lives_label = Label(self, text="Lives:3", width=10)
		lives_label.config(background=THEME_COLOR) 
		lives_label.pack(padx=10, pady=10)

		score_label = Label(self, text="Score:0", background=THEME_COLOR, width=10) 
		score_label.pack(padx=10, pady=10)

		leaderboard_button = Button(self, text="Leaderboard", command= controller.show_leaderboard)
		leaderboard_button.pack(anchor=tk.SW)

		save_button = Button(self, text="Save Score", command=controller.save_score)
		save_button.pack(anchor=tk.SE)
