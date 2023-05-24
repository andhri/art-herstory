import json
from game_logic import ArtGame
from game_interface import GameInterface

#class GameRun:
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
    
#load_data()

# id = data[random.randrange(len(data))]["objectID"]
# print(id)
# check_index = [id == i['objectID'] for i in data].index(True)
# print(check_index)

def run_game():
    '''Running the game program'''
    play = ArtGame(load_data())
    play_game = GameInterface(play)
    return play_game

if __name__ =='__main__':
    run_game()
# print(play.check_year())

# print(play_game.generate_options())

