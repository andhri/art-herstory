import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo



window = tk.Tk()
window.state('zoomed')
THEME_COLOR = "#ECDFEC"
def popup_leaderboard():
    showinfo(title='Leadership Board',
             message='Top scores!')
    #to be continued
def show_frame(frame):
    frame.tkraise()

window.rowconfigure(0, weight=3)
window.columnconfigure(0, weight=3)

welcome_frame = tk.Frame(window, bg=THEME_COLOR,) 
game_frame = tk.Frame(window)
result_frame = tk.Frame(window)

for frame in (welcome_frame, game_frame, result_frame):
    frame.grid(row=0, column=0, sticky='nsew')


#-------------Code for Welcome_frame------------------
welcome_title = tk.Label(welcome_frame, text='Welcome to "What came first?"', bg=THEME_COLOR)
welcome_title.pack(fill='x')

welcome_btn1 = tk.Button(welcome_frame, text='Play game', command=lambda:show_frame(game_frame))
welcome_btn1.pack()
# welcome_btn1.grid(column=0, row=2)
welcome_btn2 = tk.Button(welcome_frame, text='Leadership Board', command=popup_leaderboard)
welcome_btn2.pack()
# welcome_btn2.grid(column=2, row=2)
#-------------Sample for game frame--------

game_title = tk.Label(game_frame, text='Play game', bg=THEME_COLOR)
game_title.pack(fill='x')

game_btn1 = tk.Button(game_frame, text='End game', command=lambda:show_frame(result_frame))
game_btn1.pack()
#--------------sample for result frame---------
result_title = tk.Label(result_frame, text='Game Over', bg='red')
result_title.pack()

result_btn1 = tk.Button(result_frame, text='Play again', command=lambda:show_frame(game_frame))
result_btn1.pack(side= 'left')
result_btn2 = tk.Button(result_frame, text='Homepage', command=lambda:show_frame(welcome_frame))
result_btn2.pack(side= 'right')



window.mainloop()

