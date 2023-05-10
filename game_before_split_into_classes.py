from tkinter import *
from game_logic import ArtGame
from art_details import ArtDetails, file_name
from art_image import ArtImage
import json
import random
import requests
from PIL import ImageTk, Image
from io import BytesIO

THEME_COLOR = "#ECDFEC"
game_life = 3
game_score = 0

window = Tk()
# DATABASE
with open("art_database/sample_data.json", 'r') as database:
    data = json.load(database)



# GENERATE OPTIONS
def id_index(database):
    data = database
    current_id = random.randrange(len(data))
    art_id = data[current_id]["objectID"]
    id_index = [art_id == i['objectID'] for i in data].index(True)
    return id_index
def generate_option(id_index):
    art_option = data[id_index]
    return art_option


def create_image(art_option):
    url = art_option["primaryImage"]
    u = requests.get(url)
    img = Image.open(BytesIO(u.content))
    img = img.resize((400, 350), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    return img


# game options
def get_option_1():
    id_option_1 = id_index(data)
    option_1 = generate_option(id_option_1)
    return option_1
def get_image_option_1(get_option_1):
    print(get_option_1)
    image_option_1 = create_image(option_1)
    return image_option_1
def get_option_2():
    id_option_2 = id_index(data)
    option_2 = generate_option(id_option_2)
    return option_2
def get_image_option_2(get_option_2):
    print(get_option_2)
    image_option_2 = create_image(option_2)
    return image_option_2




# Game characteristics

option_1 = get_option_1()
option_2 = get_option_2()
image_option_1 = get_image_option_1(option_1)
image_option_2 = get_image_option_2(option_2)



# get user_input

# def click_option1(event):
#     # label = Label(window, text="you suck 1")
#     # label.grid(column=0, row=5)
#     print("you have selected ", 'option_1' )
#     return "option_1"
#
#
# def click_option2(event):
#     # label = Label(window, text="you suck 2")
#     # label.grid(column=1, row=5)
#     print("you have selected",'option_2' )
#     return "option_2"


# in this current state is not working properly as the years are not updating at the second click, however this is fixed once split into classes
def check_years(user_answer):
    global game_score
    global game_life
    if user_answer == "option_1" and option_1["objectEndDate"] < option_2["objectEndDate"]:
        print("year 1", option_1["objectEndDate"])
        print("year 2", option_2["objectEndDate"])
        game_score += 1
        display_art_1.config(highlightbackground="green", highlightthickness=10)
        # display_art_2.config(highlightbackground="red", highlightthickness=10)
        return True
    elif user_answer == "option_1" and option_1["objectEndDate"] > option_2["objectEndDate"]:
        game_life -= 1
        # display_art_2.config(highlightbackground="green", highlightthickness=10)
        display_art_1.config(highlightbackground="red", highlightthickness=10)
        print("year 1", option_1["objectEndDate"])
        print("year 2", option_2["objectEndDate"])
        return False
    elif user_answer == "option_2" and option_1["objectEndDate"] > option_2["objectEndDate"]:
        game_score += 1
        display_art_2.config(highlightbackground="green", highlightthickness=10)
        print("year 1", option_1["objectEndDate"])
        print("year 2", option_2["objectEndDate"])
        # display_art_1.config(highlightbackground="red", highlightthickness=10)
        return True
    elif user_answer == "option_2" and option_1["objectEndDate"] < option_2["objectEndDate"]:
        game_life -= 1
        print("year 1", option_1["objectEndDate"])
        print("year 2", option_2["objectEndDate"])
        # display_art_1.config(highlightbackground="green", highlightthickness=10)
        display_art_2.config(highlightbackground="red", highlightthickness=10)
        return False



def option_1_answer():
    give_feedback(check_years("option_1"))



def option_2_answer():
    give_feedback(check_years("option_2"))




# game_score = 0

def give_feedback(players_choice):
    score_label.config(text=f"Score:{game_score}")
    lives_label.config(text=f"Lives:{game_life}")
    window.after(1000, get_next_round)

def get_next_round():

    # global display_art_1
    # global display_art_2
    display_art_1.config(highlightbackground=THEME_COLOR, highlightthickness=0)
    display_art_2.config(highlightbackground=THEME_COLOR, highlightthickness=0)

    # print("*** BEFORE ***", display_art_1.cget('image'))
    # print("*** BEFORE ***", display_art_2.cget('image'))

    # display_art_1.grid_forget()
    # display_art_2.grid_forget()

    # print("*** MIDDLE ***", display_art_1.cget('image'))
    # print("*** MIDDLE ***", display_art_2.cget('image'))

    next_option_1 = get_option_1()
    print("this is giving this", next_option_1)
    next_option_2 = get_option_2()
    print("this is giving this", next_option_2)

    # next_image_option_1 = get_image_option_1(next_option_1)
    # print("shit is shit", next_image_option_1)
    # next_image_option_2 = get_image_option_2(next_option_2)

    # print("this is round 2 for option 2", next_image_option_2)

    url1 = next_option_1["primaryImage"]
    u = requests.get(url1)
    img1 = Image.open(BytesIO(u.content))
    img1 = img1.resize((400, 350), Image.LANCZOS)
    img1 = ImageTk.PhotoImage(img1)

    name_art_1.config(text=next_option_1["objectID"])
    name_art_2.config(text=next_option_2["objectID"])

    # image_1_label.config(image=next_image_option_1)
    # display_art_1 = Button(border_1, image=next_image_option_1, highlightthickness=0, command=option_1_answer)
    # display_art_1.grid(column=0, row=3)
    # display_art_2 = Button(border_2, image=next_image_option_2, highlightthickness=0, command=option_1_answer)
    # display_art_2.grid(column=1, row=3)

    # kanye_img = PhotoImage(file="false.png")
    # print("this is round 2", kanye_img)
    # display_art_2.config(image=kanye_img)
    # display_art_2.image = kanye_img
    # #
    #
    display_art_1.config(image=img1)
    display_art_1.image = img1
    # display_art_1.bind("<Button-1>", click_option1)


    url2 = next_option_2["primaryImage"]
    u = requests.get(url2)
    img2 = Image.open(BytesIO(u.content))
    img2 = img2.resize((400, 350), Image.LANCZOS)
    img2 = ImageTk.PhotoImage(img2)

    display_art_2.config(image=img2)
    display_art_2.image = img2
    # display_art_2.bind("<Button-1>", click_option2)



# ui
window.title("ART Game")
window.config(padx=20, pady=20, bg=THEME_COLOR)

canvas = Canvas()
canvas.config(height=600, width=500, bg=THEME_COLOR)

lives_label = Label(text="Lives:3", bg=THEME_COLOR, width=10, highlightthickness=0)
lives_label.grid(column=0, row=0)

score_label = Label(text="Score:0", bg=THEME_COLOR, width=10, highlightthickness=0)
score_label.grid(column=1, row=0)

title = Label(text="Which one came first?", bg=THEME_COLOR, width=30, highlightthickness=0, padx=20, pady=20,
              font=("Helvetica", 40, "bold"))
title.grid(column=0, row=1, columnspan=2)

# these two will have to changed into buttons for the message box to pop
name_art_1 = Label(text=option_1["objectID"], width=20, bg=THEME_COLOR, highlightthickness=0)
name_art_1.grid(column=0, row=2)

name_art_2 = Label(text=option_2["objectID"], width=20, bg=THEME_COLOR, highlightthickness=0)
name_art_2.grid(column=1, row=2)

# border_1 = Frame(window, highlightbackground=THEME_COLOR, highlightthickness=10, bd=0)

# image1 = image_option_1
# image_1_label = Label(image=image_option_1)
# image_1_label.grid(column=0, row=5)

display_art_1 = Button(image=image_option_1, highlightthickness=0, command=option_1_answer)
# print("sfsdgsd", display_art_1.cget('image'))
# display_art_1.bind("<Button-1>", click_option1)

display_art_1.grid(column=0, row=3)
# border_1.grid(column=0, row=3)

# border_2 = Frame(window, highlightbackground=THEME_COLOR, highlightthickness=0, bd=0)

display_art_2 = Button(image=image_option_2, highlightthickness=0, command=option_2_answer)
# display_art_2.bind("<Button-1>", click_option2)

display_art_2.grid(column=1, row=3)
# border_2.grid(column=1, row=3)

window.mainloop()
# def play_game(game_life):
#     print(game_life)
#     while game_life > 0:
#         game()
#
#
# play_game(game_life)
#
# print(play_game(game_life))

