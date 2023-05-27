from main import load_data
import pytest
import json

#### writing tests for the main function ####
@pytest.fixture
def mocked_art_database(monkeypatch):
    """Mock database output for testing"""
    data =[
        {
        "objectID": 1,
        "artistDisplayName": "Jane Anthony Davis",
        "title": "Lady Seated in a Boston Rocker",
        "primaryImage": "https://images.metmuseum.org/CRDImages/ad/original/ap66.242.14.jpg",
        "objectDate": "1821",
        "objectBeginDate": 1821,
        "objectEndDate": 1855
        },
        {
        "objectID": 2,
        "artistDisplayName": "Sarah Goodridge",
        "title": "Portrait of a Lady",
        "primaryImage": "https://images.metmuseum.org/CRDImages/ad/original/ap68.222.25.jpg",
        "objectDate": "1830",
        "objectBeginDate": 1830,
        "objectEndDate": 1830
        }
    ]

    def mocked_return(*args, **kwargs):
        return data
    monkeypatch.setattr("random.randrange", mocked_return)
    yield data

def test_load_data(mocked_art_database):
    """Test for the game to be loading a file"""
    expected_data = mocked_art_database

    with open("art_database/game_data_clean.json", "w") as file:
        json.dump(expected_data, file)
    
    data = load_data()
    assert data == expected_data


def test_load_data_missing_file():
    """Test for when the loading fails on the game"""
    file_name = "art_database/game_data_clean.json"
    if file_name == FileNotFoundError:
        with pytest.raises(FileNotFoundError):  
            file_name = "art_database/game_data.json"  # replace with another file