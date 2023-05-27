""" Primary Configuration file to aid in standardization """

# THEME_COLOR = "#EAF6E8"
THEME_COLOR = "#ede5d6"
CORRECT_SOUND = "game_interface/sound/correct-6033.mp3"
INCORRECT_SOUND = "game_interface/sound/incorrect-buzzer-sound-147336.mp3"
DEFAULT_FONT_COLOUR = "#FF8000"
TEXT_COLOUR = "#5f5b4c"
DEFAULT_FONT = "Garamond" # Georgia

# game logo
logo = 'game_interface/images/CFG_logo.ico'

# main_window_config
mw = 'padx=20, pady=20, background=THEME_COLOR'

# game_canvas_config
gc = 'height=600, width=500, background=THEME_COLOR'

# game_labels_config
gl = 'background=THEME_COLOR, width=10'

# game_title_config
font_title= ("Garamond", 40, "bold")

# font_body
font_body= ("Garamond", 15)

# info button
i_font = ("Garamond", 12, "italic", "bold")

# score font titles
s_font = ("Garamond", 20, "italic", "bold")

# score end_of_game title
se = ("Garamond", 30, 'bold')

# score your_score title
ss = ("Garamond", 40, 'bold')

# font buttons
bf = ("Garamond", 12, "bold")

# pop-up font
pf= ("Garamond", 15, 'bold')

# art_name_button_config
anB = 'width=30, background=THEME_COLOR'

# art_border_initial_config
abI = 'background=THEME_COLOR, bd=10'

# art_border_correct_config
abC = 'background="green", bd=10'

# art_border_incorrect_config
abIC = 'background="red", bd=10'

# cursor image
cur= 'hand2'

# game_instructions welcome page
welcome_intro = 'Welcome to the Art HerStory Game\n' \
                'Explore and play with artworks made by female artists:\n' \
                '1. Choose which was made earlier by clicking on an image.\n' \
                '2. Click on a title to see more info about the artwork.\n' \
                '3. You get a point for each correct answer.\n' \
                '4. You have 3 lives to guess before the game ends.\n' \
                '5. Can you beat your score?\n' \
                '6. Click on the "i" button if you get stuck.\n' \
                'Ready, set, GO!'

# game_instructions inside window
game_instructions ='Got stuck?\n' \
                   'These are the game instructions:\n' \
                   '1. You have 3 lives to guess before the game ends.\n' \
                   '2. You get a point for each correct answer.\n' \
                   '3. Choose which was made earlier by clicking on an image.\n' \
                   '4. Click on a title to see more info about the artwork.\n' \
                   'Have fun and good luck!'
