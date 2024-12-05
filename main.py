from tkinter import *
import pandas
import random

data = pandas.read_csv("data/french_words.csv")
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
dontknowwords = {
    "french": [],
    "english": []
}
words = data.to_dict()

def know():
    global current_card, timer
    window.after_cancel(timer)
    posi = random.randint(0, 100)
    new_word = data["French"][posi]
    canvas.itemconfig(word, text=new_word, fill="black")
    canvas.itemconfig(lang, text="French", fill="black")
    current_card["french"] = new_word
    current_card["english"] = data["English"][posi]
    canvas.itemconfig(image, image=front)
    timer = window.after(3000, func=flip_card)

def dontknow():
    global current_card, timer
    window.after_cancel(timer)
    posi = random.randint(0, 100)
    new_word = data["French"][posi]
    canvas.itemconfig(word, text=new_word, fill="black")
    canvas.itemconfig(lang, text="French", fill="black")
    current_card["french"] = new_word
    current_card["english"] = data["English"][posi]
    dontknowwords["french"] += new_word
    dontknowwords["english"] += data["English"][posi]
    ready = pandas.DataFrame.to_csv(dontknowwords, index=False)
    canvas.itemconfig(image, image=front)
    try:
        with open("data/french_words.csv", "a") as datafile:
            datafile.write(ready)
    except FileNotFoundError:
        f = open("data/french_words.csv", "w")
        f.write(ready)

    else:


    timer = window.after(3000, func=flip_card)

def flip_card():
    global current_card
    canvas.itemconfig(lang, text="English", fill="white")
    canvas.itemconfig(word, text=current_card['english'], fill="white")
    canvas.itemconfig(image, image=back)
    current_card.clear()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
front = PhotoImage(file="images/card_front.png")
back = PhotoImage(file="images/card_back.png")
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")
image = canvas.create_image(410, 270, image=front)
lang = canvas.create_text(400, 150, text="title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 250, text="word", font=("Ariel", 55, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

right_button = Button(image=right, highlightthickness=0, command=know)
right_button.grid(column=1, row=1)
wrong_button = Button(image=wrong, highlightthickness=0, command=dontknow)
wrong_button.grid(column=0, row=1)


know()



window.mainloop()
