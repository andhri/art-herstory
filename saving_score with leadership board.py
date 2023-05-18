from tkinter import *
import pickle
from tkinter import simpledialog
from datetime import datetime
THEME_COLOR = "#ECDFEC"
class ArtGameGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("ART Game")
        self.master.config(padx=20, pady=20, bg=THEME_COLOR)
        self.game_life = 3
        self.game_score = 0

        self.lives_label = Label(self.master, text="Lives:3", bg=THEME_COLOR, width=10, highlightthickness=0)
        self.lives_label.grid(column=0, row=0)

        self.score_label = Label(self.master, text="Score:0", bg=THEME_COLOR, width=10, highlightthickness=0)
        self.score_label.grid(column=1, row=0)

        self.leaderboard_button = Button(self.master, text="Leaderboard", command=self.show_leaderboard)
        self.leaderboard_button.grid(column=2, row=0)

        self.save_button = Button(self.master, text="Save Score", command=self.save_score)
        self.save_button.grid(column=3, row=0)

       

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


# Create an instance of the ArtGameGUI class
root = Tk()
game_gui = ArtGameGUI(root)
root.mainloop()