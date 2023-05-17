import json
from game_logic_try import ArtGame
from program_root import GameInterface

file_name = "sample_data_portrait.json"
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

