
BACKGROUND_COLOR = "#B1DDC6"
FONT = "Ariel"

from tkinter import *
import pandas as pd
import random

current_card = {}

try:
    word_data = pd.read_csv("data/words_to_learn.csv")
    print("loading stored data set")
except FileNotFoundError:
    word_data = pd.read_csv("data/french_words.csv")
finally:
    to_learn = word_data.to_dict(orient="records")

# ---------------------------- DISPLAY FRENCH WORDS ------------------------------- #

def next_card():
    #cancel timer
    global timer
    window.after_cancel(timer)

    #show french word
    global current_card
    current_card = random.choice(to_learn)
    card.itemconfig(card_image, image=card_front)
    card.itemconfig(language, text="French")
    card.itemconfig(word, text=current_card["French"])

    #show translation after 3 seconds
    timer = window.after(
        3000,
        show_answer,
        current_card
    )

# ---------------------------- DISPLAY ENGLISH WORDS ------------------------------- #

def show_answer(current_card_):
    global timer
    window.after_cancel(timer)
    card.itemconfig(card_image, image=card_back)
    card.itemconfig(language, text="English")
    card.itemconfig(word, text=current_card_["English"])


# ---------------------------- REMOVE KNOWN WORD ------------------------------- #

def is_known():
    global to_learn
    to_learn.remove(current_card)

    #save words to learn
    pd.DataFrame(to_learn).to_csv("data/words_to_learn.csv", index=False)

    #show next card
    next_card()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(bg="#B1DDC6", padx=50, pady=50)

timer = window.after(
    3000,
    show_answer,
    current_card
)

card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')
card = Canvas(width=800, height=526, bd=0, highlightthickness=0, background="#B1DDC6")
card_image = card.create_image(400,263,image = card_front)
language = card.create_text(400,150, text='', font=(FONT, 40, "italic"), fill="black")
word = card.create_text(400,263, text='', font=(FONT, 60, "bold"), fill="black")
card.grid(column=1,row=1,columnspan = 2)

# buttons
right_image = PhotoImage(file='images/right.png')
right_button = Button(image=right_image, highlightthickness=0, bd=0, command=is_known)
right_button.grid(column=2, row=2)

wrong_image = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_image, highlightthickness=0, bd=0, command=next_card)
wrong_button.grid(column=1, row=2)

next_card()

window.mainloop()
