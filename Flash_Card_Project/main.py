from time import sleep, time
from tkinter import *
from turtle import bgcolor 
import pandas
import random
FONT=("arial")
BACKGROUND_COLOR = "#B1DDC6"
new_words=None

# ---------------------------- add data -------------------------------------#
try:
    data=pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data=pandas.read_csv("data/french_words.csv")
    
list=[(row[0],row[1]) for (index,row) in data.iterrows()]

def random_word():
    words=random.choice(list)
    return(words)


#creating a different word
def next_word():
    global new_words
    global flip_timer
    window.after_cancel(flip_timer)
    new_words=random_word()
    canvas.itemconfig(title,text="French",fill="black")
    canvas.itemconfig(text,text=new_words[0],fill="black")
    canvas.itemconfig(img,image=card_front_img)
    flip_timer=window.after(3000,flip_card)
    
    

# ---------------------------- FLIP CARD -------------------------------------#
def flip_card():
    global new_words
    canvas.itemconfig(title,text="English",fill="white")
    canvas.itemconfig(img,image=card_back_img)
    canvas.itemconfig(text,text=new_words[1],fill="white")

 
def is_known():
    try:
        list.remove(new_words) 
        data_to_learn=pandas.DataFrame(list)
        data_to_learn.to_csv("Flash_Card_Project/data/words_to_learn.csv",index=False)
        next_word() 
        
    except :
        print("you already know all our words")   
         


# ---------------------------- UI SETUP --------------------------------------#
window=Tk()
window.config(background=BACKGROUND_COLOR,padx=50,pady=50)
window.title('FLASH CARD')

flip_timer=window.after(10,flip_card)





card_back_img=PhotoImage(file="Flash_Card_Project/images/card_back.png")
card_front_img=PhotoImage(file="Flash_Card_Project/images/card_front.png")
canvas=Canvas(height=530,width=810,highlightthickness=0,bg=BACKGROUND_COLOR)
img=canvas.create_image(405,265,image=card_front_img)
title=canvas.create_text(400,150,fill="black",text='french',font=(FONT,50,"italic"))
text=canvas.create_text(400,263,fill="black",text='word',font=(FONT,60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)

x_button_img=PhotoImage(file="Flash_Card_Project/images/wrong.png")
x_button=Button(image=x_button_img,highlightthickness=0,command=next_word)
x_button.grid(row=1,column=0)

right_button_img=PhotoImage(file="Flash_Card_Project/images/right.png")
right_button=Button(image=right_button_img,highlightthickness=0,command=is_known)
right_button.grid(row=1,column=1)


next_word()
flip_timer=window.after(3000,func=flip_card)




window.mainloop()