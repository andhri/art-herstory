# Art HerStory

## Introduction
This repository has been created for a final project of [CFG degree](https://codefirstgirls.com/courses/cfgdegree/) Software Stream Spring 2023 cohort by group OOPsies. The project is based on a game which is an adaptation of [_Higher vs Lower game_](http://www.higherlowergame.com/) and Google Arts & Culture [_What Came First?_](https://artsandculture.google.com/experiment/what-came-first/ZQGBUPErEE3bVg?hl=en). 
The game uses data extracted from [MET collections API](https://metmuseum.github.io/#object), and uses work of female artists only. 
There are significantly lower number of works by female artists in museums and galleries around the world. The National Museum of Women in the Arts, advocates for more diversity in the museums around the word, full facts can be accessed on their [website](https://nmwa.org/support/advocacy/get-facts/), some facts are:

> _"Only 13.7% of living artists represented by galleries in Europe and North America are women."_
>> _"At the Art Basel fairs (Basel, Miami, and Hong Kong), women made up less than a quarter of the artists on view over the past four years."_
>>> _"In the U.K., 64% of undergraduates and 65% of postgraduates in creative arts and design are women, but 68% of the artists represented at top London commercial galleries are men."_
>>>> _"A recent survey of the permanent collections of 18 prominent U.S. art museums found that the represented artists are 87% male and 85% white."_

## Game
Our game intends to help close this gap by highlighting the works created by female artists and raising their profile. Through playing this game, users are invited to see the the works by female artists in collection of The Metropolitan Museum of Art (MET) and engage with their works. Some of these works would often be in storage and not on current display, by engaging with the game users will benefit from experiencing works that they may not get a chance to see. They will be able to find out about female artists that they may previously not heard of and have fun guessing which artwork was created first. 

### Rules
The rules are simple:
1. You have 3 lives to guess before the game ends.
2. You get a point for each correct answer.
3. Choose which was made earlier by clicking on an image.
4. Click on a title to see more info about the artwork.

### Instructions
**To play the game please download the files as a ZIP file from this repo. The game can be run from the main.py file.**
The aim of the game is simple - guess which artwork was created first and beat current score. After running the game, a user is presented with an info message is shown explaining rules of the game, and can enter the game by pressing 'OK' button. The main window includes two images which are buttons and a user is to choose from the images which artwork was created first. A user can find out more information about the artworks by clicking on the title at the bottom of each image. If a user needs more information on how to play the game, they can click on the 'i' button to see the rules of the game again. For each correct answer user gets a point, and for each incorrect answer a user loses a life, meaning they get less incorrect attempts and less change to get better score. The game ends after user loses all their lives. The final score is added up, a user is prompted to save their score using unique name, they can also view their score history board on the last page.

## Components

### Architecture
The design of the game runs in three parts; Welcome message, main window and final score page.
![Process Flow Diagram of our project](https://github.com/andhri/art-herstory/assets/93336376/4a6a2fee-0500-406d-83c5-d04fa3f3f9ea)


### GUI
The game runs on Tkinter GUI module, some of the elements of the game are connected to the paltform's functionalities.

### Python 3
The main logic of the game is separated from the GUI elements, meaining it can be easily implemented on another platform. The principles of OOP were used for creating this game. The main logic game has unit tests attached to check its functionality. 

### Database
The data was extracted using ETL approach from [MET's API](https://metmuseum.github.io/#object), by creating variety of search terms to produce desired results. It is saved in JSON format, which was merged into main file, but other JSON files were extracted and the game can be played with a variety of these files. This can be achieved by changing the file path in t he main.py file.

## Licence 
The data extracted for this game are copyrighted from [MET's Open Acess project](https://github.com/metmuseum/openaccess). The program is not intended for mass distribution and in no event will the authors be held liable for any damages arising from the use of it. If anyone wishes to contribute to our project or have any ideas for improvement, please submit a pull request. If you indent to use any elements of this repository for any use, you are free to do so as long as you credit the original authors.
