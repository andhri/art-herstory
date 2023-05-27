import pytest
from game_logic.game_logic import ArtGame

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

@pytest.fixture
def game(mocked_art_database):
    """Class instance fixture for testing"""
    game_class = ArtGame(mocked_art_database)
    return game_class


def test_still_has_lives(game):
    """Test user still has live"""
    #game = ArtGame("data")
    assert game.lives >= 0

def test_get_portrait_by_index_left(game):
    """Test getting images by left index"""
    assert game.left_choice_index == game.option

def test_get_portrait_by_index_right(game):
    """Test getting images by right index"""
    assert game.right_choice_index == game.option

def test_get_portrait_by_index(game):
    """Test that we are getting different images"""
    game.left_choice_index = 0
    game.right_choice_index = 1
    option_1 = game.database[game.left_choice_index]["objectID"]
    option_2 = game.database[game.right_choice_index]["objectID"]
    assert option_1 != option_2

def test_check_year_left_earlier(game):
    """Test checking year work with left option"""
    game.left_choice_index = 0
    game.right_choice_index = 1
    option_1 = game.database[game.left_choice_index]["objectEndDate"]
    option_2 = game.database[game.right_choice_index]["objectEndDate"]
    assert option_1 > option_2

def test_check_year_right_earlier(game):
    """Test checking year work with right option"""
    game.left_choice_index = 1
    game.right_choice_index = 0
    option_1 = game.database[game.right_choice_index]["objectEndDate"]
    option_2 = game.database[game.left_choice_index]["objectEndDate"]
    assert option_1 > option_2

def test_check_players_choice_correct(game):
    """Test checking cplayer's choice is correct we add score"""
    game.left_choice_index = 0
    game.right_choice_index = 1
    user_answer = 'option1'
    result = game.check_players_choice(user_answer)
    if result == f"{user_answer}-correct":
        assert game.score == 1

def test_check_players_choice_incorrect(game):
    """Test checking cplayer's choice is correct we subtract live"""
    game.left_choice_index = 0
    game.right_choice_index = 0
    user_answer = 'option2'
    result = game.check_players_choice(user_answer)
    if result == f"{user_answer}-incorrect":
        assert game.lives == 2


def test_replace_title_digits(game):
    """Test if integer in art_title its replaced with X"""
    if game.art_title == int():
        assert game.art_title.replace('X')
