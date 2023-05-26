import logging
import pickle
from tkinter import Label, Button, Toplevel, Tk
from tkinter import simpledialog, messagebox
from datetime import datetime
from game_logic.game_logic import ArtGame
import game_interface.main_config as main_config

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s:%(name)s:%(message)s")

file_handler =  logging.FileHandler('logs\score.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

class SaveGameScore:
    """Initialises the second window of the game, at the end of a round"""
    def __init__(self, game_logic: ArtGame):
        self.game = game_logic
        self.master = Tk()
        self.master.title("Art HerStory")
        self.master.config(padx=20, pady=20, bg=main_config.THEME_COLOR)

        self.master.iconbitmap(main_config.logo)

        self.result = Label(self.master, text="End of game", bg=main_config.THEME_COLOR, width=20,
                            font=main_config.se, fg=main_config.TEXT_COLOUR, highlightthickness=0)
        self.result.grid(column=0, row=0, columnspan=2)

        self.score_label = Label(self.master, text=f"Your Final Score: {self.game.score}", bg=main_config.THEME_COLOR,
                                 width=20, font=main_config.ss, highlightthickness=0, fg=main_config.TEXT_COLOUR,
                                 highlightbackground=main_config.THEME_COLOR)
        self.score_label.grid(column=0, row=1, columnspan=2)

        self.score_label = Label(self.master, text="Can you beat your score?", bg=main_config.THEME_COLOR, 
                                 width=20, font=main_config.s_font, highlightthickness=0, fg=main_config.TEXT_COLOUR)
        self.score_label.grid(column=0, row=5, columnspan=2)

        self.score_label = Label(self.master, borderwidth=15, text="Almost a pro!", bg=main_config.THEME_COLOR,
                                 width=20, font=main_config.font_body, highlightthickness=0, fg=main_config.TEXT_COLOUR)
        self.score_label.grid(column=0, row=4, columnspan=2)

        self.leaderboard_button = Button(self.master, text="Score History", highlightthickness=0, fg=main_config.DEFAULT_FONT_COLOUR,
                                          activebackground=main_config.DEFAULT_FONT_COLOUR, background='white',
                                          cursor=main_config.cur, highlightcolor=main_config.DEFAULT_FONT_COLOUR,
                                          highlightbackground=main_config.THEME_COLOR, font=main_config.bf, command=self.show_leaderboard)
        self.leaderboard_button.grid(column=0, row=2)

        self.save_button = Button(self.master, text="Save Score", highlightthickness=0, fg=main_config.DEFAULT_FONT_COLOUR,
                                          activebackground=main_config.DEFAULT_FONT_COLOUR, background='white',
                                          cursor=main_config.cur, highlightcolor=main_config.DEFAULT_FONT_COLOUR,
                                          highlightbackground=main_config.THEME_COLOR, font=main_config.bf, command=self.save_score)
        self.save_button.grid(column=1, row=2)

        self.master.mainloop()

        # self.game_interface.score_update_callback = self.update_score  # Set the callback function
    def save_score(self):
        """Method to save the player's score in a pkl file with a timestamp"""
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
            logger.exception('The file was not found, creating a list.')
            leaderboard_data = []

        leaderboard_data.append(score_entry)

        with open("leaderboard.pkl", "wb") as file:
            pickle.dump(leaderboard_data, file)

    def show_leaderboard(self):
        """Method to read from the file all the previous game scores"""
        try:
            with open("leaderboard.pkl", "rb") as file:
                leaderboard_data = pickle.load(file)
        except FileNotFoundError:
            logger.exception('The file was not found, creating a list.')
            leaderboard_data = []

        leaderboard_window = Toplevel(self.master)
        leaderboard_window.title("Score History")

        for i, entry in enumerate(leaderboard_data):
            player_name = entry["Name"]
            score = entry["Score"]
            timestamp = entry["Timestamp"]

            label_text = f"{i + 1}. {player_name}: {score} points ({timestamp})"
            label = Label(leaderboard_window, text=label_text)
            label.pack()

    def get_player_name(self):
        """Method to ask the player to input their name + prompt for player if name was already used"""
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
                logger.exception('The file was not found, creating a list.')
                leaderboard_data = []

            existing_names = [entry["Name"] for entry in leaderboard_data]
            if player_name in existing_names:
                # If the name already exists, show a warning and ask for a different name
                messagebox.showwarning("Name Taken", "This name is already taken. Please enter a different name.")
            else:
                # If the name is unique, return it
                return player_name
