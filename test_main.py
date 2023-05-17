from main import load_data
import pytest
import json

#### writing tests for the main function ####

# test for the game to be loading the file
def test_load_data(tmp_path):
    file_path = tmp_path / "test_data.json"
    file_path.write_text('{"test": "data"}')
    data = load_data()
    assert data == {"test": "data"}


# test for when the loading fails on the game
def test_load_data_missing_file():
    with pytest.raises(FileNotFoundError):
        load_data()


