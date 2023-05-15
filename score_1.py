import pickle
from tkinter import Label, Button, Toplevel
from tkinter import simpledialog, messagebox
from datetime import datetime

THEME_COLOR = "#ECDFEC"

class SaveGameScore:
    def __init__(self, master, game_interface):
        self.master = master
        self.master.title("ART Game")
        self.master.config(padx=20, pady=20, bg=THEME_COLOR)
        self.game_interface = game_interface
        self.game_score = 0

        self.lives_label = Label(self.master, text="Lives:3", bg=THEME_COLOR, width=10, highlightthickness=0)
        self.lives_label.grid(column=0, row=0)

        self.score_label = Label(self.master, text="Score:0", bg=THEME_COLOR, width=10, highlightthickness=0)
        self.score_label.grid(column=1, row=0)

        self.leaderboard_button = Button(self.master, text="Leaderboard", command=self.show_leaderboard)
        self.leaderboard_button.grid(column=2, row=0)

        self.save_button = Button(self.master, text="Save Score", command=self.save_score)
        self.save_button.grid(column=3, row=0)

        self.game_interface.score_update_callback = self.update_score  # Set the callback function

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

