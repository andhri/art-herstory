import random


class ArtGame:
    """ Initialises the game logic """
    def __init__(self, database):
        self.database = database
        self.score = 0
        self.lives = 3
        self.left_choice_index = None
        self.right_choice_index = None
        self.art_title = None
        self.current_id = None
        self.option_id = None
        self.option = None

    def still_has_lives(self):
        """Method to check if the player still has lives"""
        return self.lives > 0

    def get_portrait_by_index(self, position):
        """Method to get the index of the dictionary from the list and then return a random unique option
         for option 1 and option 2"""
        self.current_id = random.randrange(len(self.database))
        self.option_id = self.database[self.current_id]["objectID"]
        self.option = [self.option_id == i['objectID'] for i in self.database].index(True)

        # print('OPTION', self.current_id)
        # print('OPTION', self.option_id)
        # print('OPTION', self.option)
        # print('LEFT', self.left_choice_index)
        # print('RIGHT', self.right_choice_index)

        if position == 'left':
            print('LEFT')
            self.left_choice_index = self.option
        elif position == 'right' and self.option == self.left_choice_index:
            # print('MIDDLE')
            # print('???????', self.option)
            # print('???????', self.left_choice_index)
            self.get_portrait_by_index('right')
        elif position == 'right':
            print('RIGHT')
            self.right_choice_index = self.option

        return self.option
    
    @staticmethod
    def check_year(year1, year2):
        """Method which compares the years """
        return year1 < year2
    
    def check_players_choice(self, user_answer):
        """ Method to check which option choice was created first """
        option_1_year = self.database[self.left_choice_index]["objectEndDate"]
        option_2_year = self.database[self.right_choice_index]["objectEndDate"]

        if (user_answer == "option_1" and self.check_year(option_1_year, option_2_year)) or (
                user_answer == "option_2" and self.check_year(option_2_year, option_1_year)):
            # print(self.database[self.left_choice_index]["objectEndDate"])
            # print(self.database[self.right_choice_index]["objectEndDate"])
            # print("before score", self.score)
            # print("after score", self.score)

            self.score += 1
            return f"{user_answer}-correct"

        elif (user_answer == "option_1" and self.check_year(option_2_year, option_1_year)) or (
                user_answer == "option_2" and self.check_year(option_1_year, option_2_year)):
            # print(self.database[self.left_choice_index]["objectEndDate"])
            # print(self.database[self.right_choice_index]["objectEndDate"])
            # print("before lives", self.lives)
            # print("after lives", self.lives)

            self.lives -= 1
            return f"{user_answer}-incorrect"

        # function for checking digits below
    
    def replace_title_digits(self, art_title):
        """ Method to check if the art title has any integers; replaces any found with an 'X' to hide possible years """
        self.art_title = art_title
        k = "X"
        for char in self.art_title:
            if char.isdigit():
                self.art_title = self.art_title.replace(char, k)
        return self.art_title
