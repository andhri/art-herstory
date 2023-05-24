import pickle
from game_logic_v4 import ArtGame
from tkinter import Label, Button, Toplevel, Tk, Frame
from tkinter import simpledialog, messagebox
from datetime import datetime
import main_config


class SaveGameScore:
    """initialises the second window of the game, at the end of a round """
    def __init__(self, game_logic: ArtGame):
        self.game = game_logic
        self.master = Tk()
        self.master.title("Art HerStory")
        self.master.config(padx=20, pady=20, bg=main_config.THEME_COLOR)

        self.result = Label(self.master, text="End of game", bg=main_config.THEME_COLOR, width=20, font='Helvetica 30 bold', highlightthickness=0)
        self.result.grid(column=0, row=0, columnspan=2)

        self.score_label = Label(self.master, text=f"Your Final Score: {self.game.score}", bg=main_config.THEME_COLOR,
                                 width=20, font='Helvetica 40 bold', highlightthickness=0,highlightbackground=main_config.THEME_COLOR)
        self.score_label.grid(column=0, row=1, columnspan=2)

        self.leaderboard_button = Button(self.master, text="Leaderboard", highlightthickness=0,
                                         highlightbackground=main_config.THEME_COLOR, command=self.show_leaderboard)
        self.leaderboard_button.grid(column=0, row=2)

        self.save_button = Button(self.master, text="Save Score", highlightthickness=0,
                                  highlightbackground=main_config.THEME_COLOR, command=self.save_score)
        self.save_button.grid(column=1, row=2)

        # self.play_again = Button(self.master, text="Play again", highlightthickness=0, command=self.run_game)
        # self.play_again.grid(column=2, row=2)

        self.master.mainloop()

        # self.game_interface.score_update_callback = self.update_score  # Set the callback function
    """function to save the player's score in a pkl file with the timestamp"""
    def save_score(self):
        player_name = self.get_player_name()  # Get the player name from the user
        if not player_name:
            # Handle case when user cancels input or enters an empty name
            return

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        score_entry = {"Name": player_name, "Score": self.game.score, "Timestamp": timestamp}

        try:
            with open("leaderboard.pkl", "rb") as file:
                leaderboard_data = pickle.load(file)
        except FileNotFoundError:
            leaderboard_data = []

        leaderboard_data.append(score_entry)

        with open("leaderboard.pkl", "wb") as file:
            pickle.dump(leaderboard_data, file)

    """function to read from the file all the previous game scores"""
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

            label_text = f"{i + 1}. {player_name}: {score} points ({timestamp})"
            label = Label(leaderboard_window, text=label_text)
            label.pack()

    """function to ask the player to input their name + propt for player if name was already used"""
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

    # def update_score(self, score):
    #
    #     self.game_score = score
    #     self.score_label.config(text=f"Score: {self.game_score}")



