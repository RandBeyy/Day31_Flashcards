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

new_word = {}
CARD_FRONT = tk.PhotoImage(file = "images/card_front.png")
CARD_BACK = tk.PhotoImage(file = "images/card_back.png")
RIGHT = tk.PhotoImage(file = "images/right.png")
WRONG = tk.PhotoImage(file = "images/wrong.png")


app_win.columnconfigure(0, weight=1)
app_win.columnconfigure(1, weight=1)
app_win.rowconfigure(0, weight=3)
app_win.rowconfigure(1, weight=1)

with open('data/french_words.csv') as f:
    french_dict = [line for line in csv.DictReader(f, fieldnames=('fr', 'en'))]

flashcard = tk.Canvas(app_win, width=800, height=526, bg=BACKGROUND_COLOR)

image = flashcard.create_image(400, 263, image=CARD_FRONT)
flashcard.grid(row=0, sticky=tk.EW, columnspan=2, padx=50)

word = flashcard.create_text((400, 263), text="Йобана", font="Arial 40 bold")
lang = flashcard.create_text((400, 150), text="Русня", font="Arial 20 italic")


def reveal_card():
    flashcard.itemconfig(image, image=CARD_BACK)
    flashcard.itemconfig(lang, text="Egnlish")
    flashcard.itemconfig(word, text=new_word["en"])
    wrong_button["state"] = "normal"
    right_button["state"] = "normal"


def next_card():
    global new_word
    new_word = choice(french_dict)
    flashcard.itemconfig(image, image=CARD_FRONT)
    flashcard.itemconfig(lang, text="French")
    flashcard.itemconfig(word, text=new_word["fr"])
    wrong_button["state"] = "disabled"
    right_button["state"] = "disabled"
    app_win.after(1000, reveal_card)
    

wrong_button = tk.Button(app_win, image=WRONG, bd=0, command=next_card)
wrong_button.grid(row=1, column=0, sticky=tk.W, padx=150)
right_button = tk.Button(app_win, image=RIGHT, bd=0, command=next_card)
right_button.grid(row=1, column=1, sticky=tk.E, padx=150)

next_card()

tk.mainloop()
