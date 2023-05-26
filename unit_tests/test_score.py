import unittest
from datetime import datetime
import pickle
from tkinter import messagebox
from game_interface.score import SaveGameScore

class GameTests(unittest.TestCase):

    def test_save_score(self):
        game = SaveGameScore()
        game.get_player_name = lambda: "Sefat"  # Mocking user input

        # Call the method under test
        game.save_score()

        # Check if the leaderboard file is created
        self.assertTrue(os.path.isfile("leaderboard.pkl"))

        # Check if the score entry is correctly saved
        with open("leaderboard.pkl", "rb") as file:
            leaderboard_data = pickle.load(file)

        self.assertEqual(len(leaderboard_data), 1)
        score_entry = leaderboard_data[0]
        self.assertEqual(score_entry["Name"], "Sefat")
        self.assertEqual(score_entry["Score"], game.game.score)

    def test_show_leaderboard(self):
        game = SaveGameScore()
        game.show_leaderboard()

        # Check if the leaderboard window is created
        self.assertTrue(game.leaderboard_window)

    def test_get_player_name(self):
        game = SaveGameScore()

        # Mocking user input
        game.simpledialog.askstring = lambda title, prompt: "Sefat"

        # Call the method under test
        player_name = game.get_player_name()

        # Check if the player name is returned correctly
        self.assertEqual(player_name, "Sefat")

    def test_update_score(self):
        game = SaveGameScore()
        score = 6

        # Call the method under test
        game.update_score(score)

        # Check if the game score and score label are updated correctly
        self.assertEqual(game.game.score, score)
        self.assertEqual(game.score_label.cget("text"), f"Score: {score}")

if __name__ == '__main__':
    unittest.main()
