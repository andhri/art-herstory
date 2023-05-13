import json

# list of all filenames
files = ['test_one', 'test_two']
# files = ["sample_data_1840_2020_hands.json",
#             "sample_data_dance.json",
#             "sample_data_landscape.json",
#             "sample_data_portrait.json",
#             "sample_data_stilllife.json",
#             "sample_data_v2.json",
#             "sample_data.json"]

# merging extracted data files into one JSON
def merge_json(filename):
    total = list()
    try:
        for f1 in filename:
            with open(f1, 'r') as infile:
                total.extend(json.load(infile))

        with open('counseling3.json', 'w') as output_file:
            json.dump(total, output_file)
    except ValueError:
        "objectID" == "objectID"

merge_json(files)
    