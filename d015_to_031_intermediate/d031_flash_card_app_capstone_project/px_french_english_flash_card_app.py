# Imports and constants.
from random import randint
from tkinter import *
import pandas
BACKGROUND_COLOR = "#B1DDC6"
current_card = None

# Attempt to find saved data from previous attempts. If none is found, load the full list.
try:
    data = pandas.read_csv('data/to_learn.csv')
except FileNotFoundError:
    data = pandas.read_csv('data/french_words.csv')
finally:
    thesaurus = data.to_dict(orient='records')


# When the user gets a card correct, remove it from the deck and draw a new card.
# This also saves progress by creating a new csv file excluding all words already solved.
def correct():
    global current_card
    thesaurus.remove(current_card)
    save = pandas.DataFrame(thesaurus)
    save.to_csv('data/to_learn.csv', index=False)
    next_card()


# When the user gets a card incorrect, leave it in the deck and draw a new card.
# After three seconds, flip the card over to reveal the English word.
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = thesaurus[randint(0, len(thesaurus)-1)]
    canvas.itemconfig(card, image=img_front)
    canvas.itemconfig(title, text='French', fill='black')
    canvas.itemconfig(word, text=current_card['French'], fill='black')
    flip_timer = window.after(3000, reveal_word)


# Flip the card over to reveal the English word.
def reveal_word():
    global current_card
    canvas.itemconfig(card, image=img_back)
    canvas.itemconfig(title, text='English', fill='white')
    canvas.itemconfig(word, text=current_card['English'], fill='white')


window = Tk()
window.title('UnfeelingRug\'s Flash Card Program')
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
img_front = PhotoImage(file='images/card_front.png')
img_back = PhotoImage(file='images/card_back.png')
card = canvas.create_image(400, 268, image=img_front)
title = canvas.create_text(400, 150, text='French -> English', font=('Comfortaa', 40, 'italic'))
word = canvas.create_text(400, 263, text='Flash Cards', font=('Comfortaa', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

img_correct = PhotoImage(file='images/right.png')
img_incorrect = PhotoImage(file='images/wrong.png')
btn_correct = Button(image=img_correct, highlightthickness=0, command=correct)
btn_correct.grid(row=1, column=1)
btn_incorrect = Button(image=img_incorrect, highlightthickness=0, command=next_card)
btn_incorrect.grid(row=1, column=0)

flip_timer = window.after(3000, next_card)

window.mainloop()
