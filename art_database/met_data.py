import json
import requests

# returns a listing of all Object IDs for objects that contain the search query ("love")  within the object’s data ("hasImages")

ids_data = requests.get(url="https://collectionapi.metmuseum.org/public/collection/v1/search?hasImages=true&q=love")
ids_data.raise_for_status()
ids = ids_data.json()
ids = ids_data.json()["objectIDs"]
print(len(ids))

ids_removed = []
full_data = []

def cleaning_data():
    for num in ids:
        # print(num)
        response = requests.get(url=f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{num}")
        # response.raise_for_status()
        data = response.json()

        if "message" in data.keys():
            # print(f"removing {num}")
            ids.remove(num)
            ids_removed.append(num)
            # print(len(ids))
            # print(ids_removed)
            # print(f"removed {num}")


        else:
            if data["artistGender"] == "Female" and data["primaryImage"] != "":
                art_dict = {}
                art_dict["objectID"] = data["objectID"]
                art_dict["artistDisplayName"] = data["artistDisplayName"]
                # print(art_dict["artistDisplayName"])
                # print(data["artistDisplayName"])
                art_dict["title"] = data["title"]
                art_dict["artistGender"] = data["artistGender"]
                art_dict["primaryImage"] = data["primaryImage"]
                art_dict["culture"] = data["culture"]
                art_dict["country"] = data["country"]
                art_dict["artistWikidata_URL"] = data["artistWikidata_URL"]
                art_dict["objectDate"] = data["objectDate"]
                art_dict["objectBeginDate"]= data["objectBeginDate"]
                art_dict["objectEndDate"] = data["objectEndDate"]
                full_data.append(art_dict)
                # print(full_data)
                # print(art_dict)


    with open("sample_data.json", "w+") as file:
        file.write(json.dumps(full_data))
#
cleaning_data()

print(len(full_data))
print(full_data)
print(len(ids_removed))
