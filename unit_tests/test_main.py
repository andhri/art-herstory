import pytest

#### writing tests for the main function ####

DATA = 'data'
def test_load_data(tmp_path):
    """Test for the game to be loading a file from temp directory"""
    d = tmp_path / "dict"
    d.mkdir()
    p = d / "test data"
    p.write_text(DATA)
    assert p.read_text() == DATA
    assert len(list(tmp_path.iterdir())) == 1



def test_load_data_missing_file():
    """Test for when the loading fails on the game"""
    file_name = "art_database/game_data_clean.json"
    if file_name == FileNotFoundError:
        with pytest.raises(FileNotFoundError):  
            file_name = "art_database/game_data.json"  # replace with another file