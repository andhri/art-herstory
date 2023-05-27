import logging
import json
from game_logic.game_logic import ArtGame
from game_interface.game_interface import GameInterface
from game_interface.game_answers import GameAnswers
from game_interface.game_options import ArtOptions
from game_interface.display import DisplayConfig
from game_interface.parent_interface import Parent

# Log for exceptions
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s:%(name)s:%(message)s")

file_handler =  logging.FileHandler('logs\main.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


# Loading data onto the game
def load_data():
    """ Loading data in the game """
    try:
        file_name = "art_database/game_data_clean.json"  
        with open(file_name, 'r') as database:
            data = json.load(database)
            return data
    except FileNotFoundError:  # exception for when the file fails to load, load another file
        logger.exception('The file was not found, using alternative file.')
        file_name = "art_database/game_data.json"
        with open(file_name, 'r') as database:
            data = json.load(database)
            return data


# Main program
def run_game():
    """ Running the game program """
    play = ArtGame(load_data())
    parent = Parent()
    display = DisplayConfig(parent, play)
    answers = GameAnswers(parent, play, display)
    art_options = ArtOptions(parent, play, display)
    play_game = GameInterface(parent, play, art_options, answers, display)
    return play_game


# running the game
if __name__ == '__main__':
    run_game()
