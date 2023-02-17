import tkinter as tk
from tkinter import ttk
#from settings import Settings
from random import choice
import csv

BACKGROUND_COLOR = "#B1DDC6"

app_win = tk.Tk()
app_win.geometry("900x726")
app_win.title("Main app_window")
app_win.configure(bg=BACKGROUND_COLOR)


CARD_FRONT = tk.PhotoImage(file = "images/card_front.png")
CARD_BACK = tk.PhotoImage(file = "images/card_back.png")
RIGHT = tk.PhotoImage(file = "images/right.png")
WRONG = tk.PhotoImage(file = "images/wrong.png")


app_win.columnconfigure(0, weight=1)
app_win.columnconfigure(1, weight=1)
app_win.rowconfigure(0, weight=3)
app_win.rowconfigure(1, weight=1)

flashcard = tk.Canvas(app_win, width=800, height=526, bg=BACKGROUND_COLOR)
image = flashcard.create_image(400, 263, image=CARD_FRONT)
flashcard.grid(row=0, sticky=tk.EW, columnspan=2, padx=50)


wrong_button = tk.Button(app_win, image=WRONG, bd=0).grid(row=1, column=0, sticky=tk.W, padx=150)
right_button = tk.Button(app_win, image=RIGHT, bd=0).grid(row=1, column=1, sticky=tk.E, padx=150)




tk.mainloop()
