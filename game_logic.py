from tkinter import *
import random


class ArtGame():
    def __init__(self, database):
        self.database = database
        self.score = 0
        self.lives = 3
        self.current_id_1= None
        self.current_id_2 = None

    def still_has_lives(self):
        return self.lives > 0

    def get_option_1(self):
        self.current_id_1 = random.randrange(len(self.database))
        self.option_1_id = self.database[self.current_id_1]["objectID"]
        self.option_1 = [self.option_1_id == i['objectID'] for i in self.database].index(True)

        return self.option_1

    def get_option_2(self):
        self.current_id_2 = random.randrange(len(self.database))
        self.option_2_id = self.database[self.current_id_2]["objectID"]
        self.option_2 = [self.option_2_id == i['objectID'] for i in self.database].index(True)
        return self.option_2


    def check_year(self, user_answer):
        if user_answer == "option_1" and self.database[self.option_1]["objectEndDate"] < self.database[self.option_2]["objectEndDate"]:
            print(self.database[self.option_1]["objectEndDate"])
            print(self.database[self.option_2]["objectEndDate"])
            print("before score", self.score)
            self.score += 1
            print("after score", self.score)
            return "user's option_1 correct"

            # return True
        elif user_answer == "option_1" and self.database[self.option_1]["objectEndDate"] > self.database[self.option_2]["objectEndDate"]:
            print(self.database[self.option_1]["objectEndDate"])
            print(self.database[self.option_2]["objectEndDate"])
            print("before lives", self.lives)
            self.lives -= 1
            print("after lives", self.lives)
            return "user's option_1 incorrect"


        elif user_answer == "option_2" and self.database[self.option_2]["objectEndDate"] < self.database[self.option_1]["objectEndDate"]:
            print(self.database[self.option_1]["objectEndDate"])
            print(self.database[self.option_2]["objectEndDate"])
            print("before score", self.score)
            self.score += 1
            print("before score", self.score)
            # display_art_2.config(highlightbackground="green", highlightthickness=10)
            return "user's option_2 correct"

        elif user_answer == "option_2" and  self.database[self.option_2]["objectEndDate"] > self.database[self.option_1]["objectEndDate"]:
            print(self.database[self.option_1]["objectEndDate"])
            print(self.database[self.option_2]["objectEndDate"])
            print("before lives", self.lives)
            self.lives -= 1
            print("after lives", self.lives)
            return "user's option_2 incorrect"








