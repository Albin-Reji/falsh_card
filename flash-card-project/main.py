from tkinter import *
import pandas
import  random
BACKGROUND_COLOR = "#B1DDC6"
current_card={}
to_learn={}
try:
    data=pandas.read_csv("data/words_to_learn")
except FileNotFoundError:
    original_data=pandas.read_csv("data/french_words.csv")
    to_learn=original_data.to_dict(orient="records")
else:
    to_learn= data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card['French'])
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer=window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card['English'])
    canvas.itemconfig(card_background, image=card_back_image)

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data=pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn", index=False)
    pandas.read_csv("data/words_to_learn")
    next_card()


# creating screen
window= Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flashy")
flip_timer=window.after(3000, flip_card)


# canvas created
canvas=Canvas(width=800, height=526,bg=BACKGROUND_COLOR,  highlightthickness=0)
card_front_image=PhotoImage(file="/python(workspace)/flash-card-project/images/card_front.png")
card_back_image=PhotoImage(file="/python(workspace)/flash-card-project/images/card_back.png")
card_background=canvas.create_image(400,263, image=card_front_image)
card_title=canvas.create_text(400, 150,text="Title", font=("Arial", 40, "italic"))
card_word=canvas.create_text(400, 263,text="Word", font=("Arial", 50, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# button creating
# correct_button creating
right_button_img=PhotoImage(file="./images/right.png")
right_button=Button(image=right_button_img,highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
right_button.grid(row=1, column=1)
#
# wrong_burron creating
wrong_button_img=PhotoImage(file="./images/wrong.png")
wrong_button=Button(image=wrong_button_img,bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)


next_card()

window.mainloop()