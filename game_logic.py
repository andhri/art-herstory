from tkinter import *
import random


class ArtGame:
    def __init__(self, database):
        self.database = database
        self.score = 0
        self.lives = 3
        self.left_choice_index = None
        self.right_choice_index = None

    def still_has_lives(self):
        return self.lives > 0

    def get_portrait_by_index(self, position):
        self.current_id = random.randrange(len(self.database))
        self.option_id = self.database[self.current_id]["objectID"]
        self.option = [self.option_id == i['objectID'] for i in self.database].index(True)

        if (position == 'left'):
            self.left_choice_index = self.option
        elif (position == 'right' and self.option != self.left_choice_index):
            print(self.option != self.left_choice_index)
            print(self.option)
            print(self.left_choice_index)
            self.right_choice_index = self.option

        return self.option

    def check_year(self):
        return self.database[self.left_choice_index]["objectEndDate"] < self.database[self.right_choice_index]

    def check_players_choice(self, user_answer):
        if (user_answer == "option_1" and self.database[self.left_choice_index]["objectEndDate"] < \
            self.database[self.right_choice_index][
                "objectEndDate"]) or (
                user_answer == "option_2" and self.database[self.right_choice_index]["objectEndDate"] < \
                self.database[self.left_choice_index][
                    "objectEndDate"]):

            # print(self.database[self.left_choice_index]["objectEndDate"])
            # print(self.database[self.right_choice_index]["objectEndDate"])
            # print("before score", self.score)
            # print("after score", self.score)

            self.score += 1

            return f"{user_answer}-correct"


        elif (user_answer == "option_1" and self.database[self.left_choice_index]["objectEndDate"] > \
              self.database[self.right_choice_index][
                  "objectEndDate"]) or (
                user_answer == "option_2" and self.database[self.right_choice_index]["objectEndDate"] > \
                self.database[self.left_choice_index][
                    "objectEndDate"]):
            # print(self.database[self.left_choice_index]["objectEndDate"])
            # print(self.database[self.right_choice_index]["objectEndDate"])
            # print("before lives", self.lives)
            # print("after lives", self.lives)

            self.lives -= 1

            return f"{user_answer}-incorrect"
