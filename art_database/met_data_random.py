import json
import requests
import random


# returns a listing of all Object IDs
ids_data = requests.get(url="https://collectionapi.metmuseum.org/public/collection/v1/objects")
ids_data.raise_for_status()
ids = ids_data.json()
ids = ids_data.json()["objectIDs"]
print(len(ids))

ids_removed = []
full_data = []

# runs through the payload to check which ones have female gender and image and writes the data into a json file
def cleaning_data():
    for num in random.sample(ids, 7000):
        response = requests.get(url=f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{num}")
        # response.raise_for_status()
        data = response.json()

        if "message" in data.keys():
            ids.remove(num)
            ids_removed.append(num)

        else:
            if data["artistGender"] == "Female" and data["primaryImage"] != "":
                art_dict = {}
                art_dict["objectID"] = data["objectID"]
                art_dict["artistDisplayName"] = data["artistDisplayName"]
                art_dict["title"] = data["title"]
                art_dict["artistGender"] = data["artistGender"]
                art_dict["primaryImage"] = data["primaryImage"]
                art_dict["culture"] = data["culture"]
                art_dict["country"] = data["country"]
                art_dict["objectDate"] = data["objectDate"]
                art_dict["objectBeginDate"]= data["objectBeginDate"]
                art_dict["objectEndDate"] = data["objectEndDate"]
                full_data.append(art_dict)

    with open("sample_data_v2.json", "w+") as file:
        file.write(json.dumps(full_data))
cleaning_data()

# print(len(full_data))
# print(full_data)
# print(len(ids_removed))
