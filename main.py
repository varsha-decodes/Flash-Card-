from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

#-------------------------------Creating dataframe-------------------------#
current_card = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    og_data = pandas.read_csv("data/french_words.csv")
    data_dict = og_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")
# list of dicts containing 2 elements each


#------------------------------Functionality----------------------------#
def flip_card():
    canvas.itemconfig(title, text="English",fill= "white")
    canvas.itemconfig(word, text= current_card['English'],fill="white")
    canvas.itemconfig(card_image, image=card_back_image)

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(card_image,image = card_front_image)
    canvas.itemconfig(title, text="French",fill = BACKGROUND_COLOR)
    canvas.itemconfig(word, text=current_card['French'],fill = BACKGROUND_COLOR)
    flip_timer=window.after(3000,func=flip_card)

def is_known():
    data_dict.remove(current_card)
    df = pandas.DataFrame(data_dict)
    df.to_csv("data/words_to_learn.csv",index=False)
    next_card()

# -------------------------------Frontend------------------------------#
window = Tk()
window.title("Flashy")
window.config(padx=40, pady=40, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000,flip_card)

card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")

canvas = Canvas(height=526,width=800,bg=BACKGROUND_COLOR,highlightbackground=BACKGROUND_COLOR)
card_image = canvas.create_image(400,263, image=card_front_image)
title = canvas.create_text(400,150,text="",fill=BACKGROUND_COLOR,font=("Ariel",40,"italic"))
word = canvas.create_text(400,263,text="",fill=BACKGROUND_COLOR,font= ("Ariel",60,"bold"))
canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image,highlightcolor=BACKGROUND_COLOR,highlightbackground=BACKGROUND_COLOR,command=is_known)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image,highlightcolor=BACKGROUND_COLOR,highlightbackground=BACKGROUND_COLOR,command=next_card)

wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()
