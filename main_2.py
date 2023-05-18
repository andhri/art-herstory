import json
from game_logic_v3 import ArtGame
from game_interface_v3 import GameInterface
from game_answers import GameAnswers
from game_options import ArtOptions
from display import DisplayConfig


# class GameRun:
# add an exception here for when the file fails to load, load another file
def load_data():
    """Loading data onto game"""
    try:
        file_name = "art_database/game_data.json"
        with open(file_name, 'r') as database:
            data = json.load(database)
            return data
    except FileNotFoundError:
        file_name = "art_database\sample_data_portrait.json"
        with open(file_name, 'r') as database:
            data = json.load(database)
            return data


# load_data()

# id = data[random.randrange(len(data))]["objectID"]
# print(id)
# check_index = [id == i['objectID'] for i in data].index(True)
# print(check_index)

def run_game():
    '''Running the game program'''
    play = ArtGame(load_data())
    answers = GameAnswers()
    display = DisplayConfig(play)
    art_options = ArtOptions(play, answers, display)

    play_game = GameInterface(play, art_options, answers, display)
    return play_game


if __name__ == '__main__':
    run_game()
# print(play.check_year())