import json
from game_logic import ArtGame
from game_interface import GameInterface


# add an exception here for when the file fails to load, load another file
try:
    file_name = "art_database/game_data.json"
    with open(file_name, 'r') as database:
        data = json.load(database)
except FileNotFoundError:
    file_name = "art_database\sample_data_portrait.json"
    with open(file_name, 'r') as database:
        data = json.load(database)


# id = data[random.randrange(len(data))]["objectID"]
# print(id)
# check_index = [id == i['objectID'] for i in data].index(True)
# print(check_index)

play = ArtGame(data)
play_game = GameInterface(play)
# print(play.check_year())

# print(play_game.generate_options())

