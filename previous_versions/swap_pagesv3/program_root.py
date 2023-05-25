import tkinter as tk
from tkinter import *
from frames import StartPage, ResultPage, GamePage
from game_logic_try import ArtGame
import pickle
from PIL import ImageTk, Image
import requests
from io import BytesIO
import pygame
from tkinter import simpledialog, messagebox
from datetime import datetime

# GamePage
# from mira_update.game_interface_v3 import GamePage
# from tkinter.messagebox import showinfo

LARGEFONT =("Verdana", 16)
THEME_COLOR = "#EAF6E8"
CORRECT_SOUND = "correct-6033.mp3"
INCORRECT_SOUND = "incorrect-buzzer-sound-147336.mp3"

class GameInterface(tk.Tk):
	def __init__(self, art_game = ArtGame):  # art_game: ArtGame
		self.game = art_game
		self.frames = StartPage, ResultPage, GamePage
		tk.Tk.__init__(self)
		
		container = tk.Frame(self)
		container.pack(side = "top", fill = "both", expand = True)
		container.config(padx=20, pady=20, bg=THEME_COLOR)
		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)
		self.lives = 3
		self.score = 0
		self.frames = {}

		for F in (StartPage, ResultPage, GamePage):  #GamePage

			frame = F(container, self)

			self.frames[F] = frame
			frame.grid(row = 0, column = 0, sticky ="nsew")

		self.show_frame(StartPage)
    
		# self.generate_options()

	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()


	def save_score(self):
		player_name = self.get_player_name()  # Get the player name from the user
		if not player_name:
			# Handle case when user cancels input or enters an empty name
			return

		timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		score_entry = {"Name": player_name, "Score": self.game_score, "Timestamp": timestamp}

		try:
			with open("leaderboard.pkl", "rb") as file:
				leaderboard_data = pickle.load(file)
		except FileNotFoundError:
			leaderboard_data = []

		leaderboard_data.append(score_entry)

		with open("leaderboard.pkl", "wb") as file:
			pickle.dump(leaderboard_data, file)

	def show_leaderboard(self):
		try:
			with open("leaderboard.pkl", "rb") as file:
				leaderboard_data = pickle.load(file)
		except FileNotFoundError:
			leaderboard_data = []

		leaderboard_window = Toplevel(self.master)
		leaderboard_window.title("Leaderboard")

		for i, entry in enumerate(leaderboard_data):
			player_name = entry["Name"]
			score = entry["Score"]
			timestamp = entry["Timestamp"]

			label_text = f"{i+1}. {player_name}: {score} points ({timestamp})"
			label = Label(leaderboard_window, text=label_text)
			label.pack()

	def get_player_name(self):
		while True:
			player_name = simpledialog.askstring("Player Name", "Enter your name:")

			if not player_name:
				# Handle case when user cancels input or enters an empty name
				return None

			# Check if the name already exists in the leaderboard
			try:
				with open("leaderboard.pkl", "rb") as file:
					leaderboard_data = pickle.load(file)
			except FileNotFoundError:
				leaderboard_data = []

			existing_names = [entry["Name"] for entry in leaderboard_data]
			if player_name in existing_names:
				# If the name already exists, show a warning and ask for a different name
				messagebox.showwarning("Name Taken", "This name is already taken. Please enter a different name.")
			else:
				# If the name is unique, return it
				return player_name

	def update_score(self, score):
		
			self.game_score = score
			self.score_label.config(text=f"Score: {self.game_score}")

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
		self.after(1000, self.generate_options)
# Driver Code
app = GameInterface()
app.mainloop()


