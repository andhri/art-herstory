import tkinter as tk
from tkinter import ttk
from tkinter import *
from game_logic import ArtGame
import pickle
from tkinter import simpledialog
from datetime import datetime
# from tkinter.messagebox import showinfo
# from result import show_leaderboard
LARGEFONT =("Verdana", 16)
THEME_COLOR = "#ECDFEC"
class GameInterface(tk.Tk):
	
	# __init__ function for class tkinterApp
	def __init__(self, *arg, **kwargs):  # art_game: ArtGame
		# self.game = art_game
		# __init__ function for class Tk
		tk.Tk.__init__(self)
		# creating a container
		container = tk.Frame(self)
		container.pack(side = "top", fill = "both", expand = True)
		container.config(padx=20, pady=20, bg=THEME_COLOR)
		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		# initializing frames to an empty array
		self.frames = {}

		# iterating through a tuple consisting
		# of the different page layouts
		for F in (StartPage, GamePage, ResultPage):

			frame = F(container, self)

			# initializing frame of that object from
			# startpage, GamePage, ResultPage respectively with
			# for loop
			self.frames[F] = frame

			frame.grid(row = 0, column = 0, sticky ="nsew")

		self.show_frame(StartPage)
    
    # def open_popup(self):
    #     popup = PopupWindow(self)
    #     popup.grab_set()
    #     self.wait_window(popup)
	# to display the current frame passed as
	# parameter
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()
	
	def save_score(self):
		player_name = self.get_player_name()  # Get the player name from the user
		timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		score_entry = {"Name": player_name, "Score": self.game_score, "Timestamp": timestamp}
		
		try:
			with open("leaderboard.pkl", "rb") as file:
				leaderboard = pickle.load(file)
		except FileNotFoundError:
			leaderboard = []
			
		leaderboard.append(score_entry)

		with open("leaderboard.pkl", "wb") as file:
			pickle.dump(leaderboard, file)

	def show_leaderboard(self):
		try:
			with open("leaderboard.pkl", "rb") as file:
				leaderboard = pickle.load(file)
		except FileNotFoundError:
			leaderboard = []
		
		leaderboard_window = Toplevel(self.master)
		leaderboard_window.title("Leaderboard")

		for i, entry in enumerate(leaderboard):
			player_name = entry["Name"]
			score = entry["Score"]
			timestamp = entry["Timestamp"]

			label_text = f"{i+1}. {player_name}: {score} points ({timestamp})"
			label = Label(leaderboard_window, text=label_text)
			label.pack()

	def get_player_name(self):
		player_name = simpledialog.askstring("Player Name", "Enter your name:")
		return player_name
	
	# def show_Leaderboard(self):
	# 	pop = Toplevel(self.master)
	# 	pop.title("Leaderboard")
	# 	pop_Label = Label(pop, text="Top 10 scores!")
	# 	pop_Label.grid(row = 0, column = 0, sticky ="nsew")
	# 	# leaderboard = Label(pop, text=f'{show_leaderboard}')
	# 	my_frame = Frame(pop, bg=THEME_COLOR)
	# 	my_frame.grid(row = 0, column = 0, sticky ="nsew")

# first window frame startpage
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


		button1 = ttk.Button(self, text ="Play Game",
		command = lambda : controller.show_frame(GamePage))
	
		# putting the button in its place by
		# using grid
		button1.grid(row = 2, column = 0, padx = 10, pady = 10)

		## button to show frame 2 with text layout2
		button2 = ttk.Button(self, text ="Leaderboard",
		command = controller.show_leaderboard)
	
		# putting the button in its place by
		# using grid
		button2.grid(row = 2, column = 3, padx = 10, pady = 10)
	def do_button(self):
		page = self.controller.get_page(ResultPage)
		page.function()
       
# second window frame GamePage
class GamePage(tk.Frame):
	
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		
		label = ttk.Label(self, text ="Page 1", font = LARGEFONT)
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		# button to show frame 2 with text
		# layout2
		button1 = ttk.Button(self, text ="StartPage",
							command = lambda : controller.show_frame(StartPage))
	
		# putting the button in its place
		# by using grid
		button1.grid(row = 1, column = 1, padx = 10, pady = 10)

		# button to show frame 2 with text
		# layout2
		button2 = ttk.Button(self, text ="EndGame",
							command = lambda : controller.show_frame(ResultPage))
	
		# putting the button in its place by
		# using grid
		button2.grid(row = 2, column = 1, padx = 10, pady = 10)




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
		
       

            

# Driver Code
app = GameInterface()
app.mainloop()


