from tkinter import *
from game_interface_v2 import GameInterface
from game_options import ArtOptions
from game_logic_v3 import ArtGame


class InfoPopUp(Toplevel):

    def __init__(self, game_logic: ArtGame):
        Toplevel.__init__(self)
        self.geometry("400x200")
        self.title("Additional Information")
        self.art_options = ArtOptions
        self.game_logic = game_logic

        main_label = Label(self, text="Here is some more information about this piece:",
                                 font="Helvetica 13", pady=20, padx=60)
        main_label.pack()
        main_label.grid()

        info_label1 = Label(self, text=self.add_info_1, font='Helvetica 13')
        info_label1.grid()

        info_label2 = Label(self, text=self.add_info_2, font='Helvetica 13')
        info_label2.grid()

        self.add_info_1 = None
        self.add_info_2 = None

        button = Button(text="Close", command=lambda: self.close_popup())
        button.grid(row=1)

        self.option_1 = self.game_logic.get_portrait_by_index('left')
        print(self.game_logic.database[self.option_1])
        self.option_2 = self.game_logic.get_portrait_by_index('right')
        print(self.game_logic.database[self.option_2])

    def add_info_by_option(self):
        # self.add_info_1 = self.option_1["artistDisplayName", "country", "culture"]
        # self.add_info_2 = self.option_2["artistDisplayName", "country", "culture"]

        # this function isn't ready yet and still working on it....
        if self.art_options.generate_options().option_1:
            self.add_info_1 = self.art_options.generate_options().option_1["artistDisplayName", "country", "culture"]
            print(self.add_info_1)

        elif self.art_options.generate_options().option_2:
            self.add_info_2 = self.art_options.generate_options().option_2["artistDisplayName", "country", "culture"]
            print(self.add_info_2)

    def close_popup(self):
        self.destroy()




