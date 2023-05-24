import json

# list of all filenames
files = ["art_database\sample_data_1840_2020_hands.json",
         "art_database\sample_data_dance.json",
         "art_database\sample_data_landscape.json",
         "art_database\sample_data_portrait.json",
         "art_database\sample_data_stilllife.json",
         "art_database\sample_data_random.json",
         "art_database\sample_data_love.json",
         "art_database\sample_data_abstract.json"
          ]

# merging extracted data files into one JSON
def merge_json(filename):
    all_data = []
    unique_ids= set()
    # unique_dates = set()
    try:
        for file in filename:
            with open(file, 'r') as infile:
                data = json.load(infile)
                for item in data:
                    if item['objectID'] not in unique_ids: # and item['objectEndDate'] not in unique_dates:
                        unique_ids.add(item['objectID'])
                        # unique_dates.add(item['objectEndDate'])
                        all_data.append(item)
        sorted_data = sorted(all_data, key=lambda d: d["objectID"])
    except Exception as err:
        return f"Error: {err}."
    else:
        with open('art_database\game_data.json', 'w+') as output_file:
            json.dump(sorted_data, output_file, indent=4)
            print(len(all_data))

merge_json(files)
    
