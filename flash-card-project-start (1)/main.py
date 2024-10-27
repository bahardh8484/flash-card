BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import json
import random
import pandas
import json
list = {}
current_card = {}
try:
    with open("data\words_to_learn!!") as file:
         data = pandas.read_csv(file)
except FileNotFoundError:
    org = pandas.read_csv("data\Hfrench_words.csv")
    list = org.to_dict(orient="records")
else:
  list = data.to_dict(orient="records")

def next_card():
        global current_card,next,list
        window.after_cancel(next)
        current_card = random.choice(list)
        canvas.itemconfig(title, text="French",fill = "black")
        canvas.itemconfig(word,text = current_card["French"],fill = "black")
        canvas.itemconfig(old_image,image = white_card)
        next = window.after(3000, change_card)

def is_known():

    list.remove(current_card)
    unknown = pandas.DataFrame(list)
    unknown.to_csv("data\words_to_learn!!",index=False)
    next_card()
def change_card():
    canvas.itemconfig(title,text = 'English')
    canvas.itemconfig(word, text=current_card["English"])
    canvas.itemconfig(word,fill = "white")
    canvas.itemconfig(title, fill="white")
    canvas.itemconfig(old_image,image =new_image)
window = Tk()
window.title("flashy")
window.config(bg = BACKGROUND_COLOR,padx = 50,pady = 50)
next = window.after(3000,change_card)
white_card = PhotoImage(file = "images\card_front.png")
new_image = PhotoImage(file="images\card_back.png")
canvas = Canvas(width=800,height=526,bg = BACKGROUND_COLOR,highlightthickness=0)
old_image = canvas.create_image(400,263,image = white_card)
title = canvas.create_text(400 ,150 , text = "",font = ("Ariel",40,"italic"))
word = canvas.create_text(400 ,263 , text = "",font = ("Ariel",60,"bold"))
canvas.grid(column = 0 , row = 0 , columnspan = 2)
x_image = PhotoImage(file="images\wrong.png")
x_buttom = Button(image=x_image, highlightthickness=0, command=next_card)
x_buttom.grid(column = 0 , row = 1)
r_image = PhotoImage(file="images\click.png")
r_buttom = Button(image=r_image, highlightthickness=0, command=is_known)
r_buttom.grid(column = 1 , row = 1)








next_card()







window.mainloop()