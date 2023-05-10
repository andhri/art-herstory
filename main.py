import json
from game_logic import ArtGame
from game_interface import GameInterface

file_name = "art_database/sample_data.json"
with open(file_name, 'r') as database:
    data = json.load(database)


# id = data[random.randrange(len(data))]["objectID"]
# print(id)
# check_index = [id == i['objectID'] for i in data].index(True)
# print(check_index)

play = ArtGame(data)
print(play.get_option_1(), play.get_option_2())
play_game = GameInterface(play)
# print(play.check_year())

# print(play_game.generate_options())

