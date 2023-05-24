import tkinter as tk
from tkinter import ttk
from tkinter import *
from game_logic_try import ArtGame
LARGEFONT =("Verdana", 16)
THEME_COLOR = "#ECDFEC"

class StartPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		
		# label of frame Layout 2
		label = ttk.Label(self, text ='Welcome to "ArtGame"', font = LARGEFONT)
		
		# putting the grid in its place by using
		# grid
		label.grid(row = 0, column = 1, padx = 10, pady = 10)

		instructions = ttk.Label(self, text='Instructions')
		instructions.grid(row=1, column=1)


		button1 = ttk.Button(self, text ="Play Game",command = lambda : controller.show_frame(GamePage))
	
		# putting the button in its place by
		# using grid
		button1.grid(row = 2, column = 0, padx = 10, pady = 10)

		## button to show frame 2 with text layout2
		button2 = ttk.Button(self, text ="Leaderboard",
		command = controller.show_leaderboard)
	
		# putting the button in its place by
		# using grid
		button2.grid(row = 2, column = 3, padx = 10, pady = 10)

 
# second window frame GamePage
class GamePage(tk.Frame):
	
	def __init__(self, parent, controller, art_game = ArtGame):
		tk.Frame.__init__(self)
		self.lives = art_game.lives
		self.score = art_game.score
		self.lives_label = Label(text=f"Lives:{self.lives}", bg=THEME_COLOR, width=10, highlightthickness=0)
		self.lives_label.grid(column=0, row=0)

		self.score_label = Label(text=f"Score:{self.score}", bg=THEME_COLOR, width=10, highlightthickness=0)
		self.score_label.grid(column=1, row=0)

		self.title = Label(text="Which one came first?", bg=THEME_COLOR, width=30, highlightthickness=0, padx=20,
							pady=20, font=("Helvetica", 40, "bold"))
		self.title.grid(column=0, row=1, columnspan=2)

		self.name_art_1 = Button(text="option_1.art_name", width=40, bg=THEME_COLOR)
		self.name_art_1.bind('<Configure>', lambda e: self.name_art_2.config(wraplength=self.name_art_2.winfo_width()))
		self.name_art_1.grid(column=0, row=3)

		self.name_art_2 = Button(text="option_2.art_name", width=40, bg=THEME_COLOR)
		self.name_art_2.bind('<Configure>', lambda e: self.name_art_2.config(wraplength=self.name_art_2.winfo_width()))
		self.name_art_2.grid(column=1, row=3)

	# -----------------------------------------------------------------------------------------------

		self.border_1 = LabelFrame(background=THEME_COLOR, bd=10)
		self.border_1.grid(column=0, row=2, padx=20, pady=20)

		self.display_art_1 = Button(self.border_1, text="Option 1", highlightthickness=0)
		self.display_art_1.grid(column=0, row=2)

		self.border_2 = LabelFrame(background=THEME_COLOR, bd=10)
		self.border_2.grid(column=1, row=2, padx=20, pady=20)

		self.display_art_2 = Button(self.border_2, text="Option 2", highlightthickness=0)
		self.display_art_2.grid(column=1, row=2)


# third window frame page
class ResultPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		lives_label = ttk.Label(self, text="Lives:3", background=THEME_COLOR, width=10)  #highlightthickness=0
		lives_label.grid(column=0, row=0)

		score_label = ttk.Label(self, text="Score:0", background=THEME_COLOR, width=10)  #highlightthickness=0
		score_label.grid(column=1, row=0)

		leaderboard_button = ttk.Button(self, text="Leaderboard", command= controller.show_leaderboard)
		leaderboard_button.grid(column=2, row=0)

		save_button = ttk.Button(self, text="Save Score", command=controller.save_score)
		save_button.grid(column=3, row=0)
