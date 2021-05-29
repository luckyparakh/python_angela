from tkinter import *
import pandas
from time import sleep

# from Tkinter.FlashCardProjectStart.images
BACKGROUND_COLOR = "#B1DDC6"
COUNT = 3
F_IMG = r'C:\1\learn\py\angela_yu\python_angela\Tkinter\FlashCardProjectStart\images\card_front.png'
E_IMG = './images/card_back.png'


timer = None
timer_ms = 1800

try:
    with open('./data/word_to_learn.csv'):
        csv_data = pandas.read_csv('./data/word_to_learn.csv')
except FileNotFoundError:
    csv_data = pandas.read_csv('./data/french_words.csv')
sample = csv_data.sample()


def right():
    global sample, timer
    reset_screen('French', f_img)
    csv_data.drop(index=sample.index, inplace=True)
    csv_data.to_csv('./data/word_to_learn.csv', index=False)
    sample = csv_data.sample()
    canvas.itemconfig(word, text=sample.French.values[0])
    timer = window.after(timer_ms, flip)


def wrong():
    global sample, timer
    reset_screen('French', f_img)
    sample = csv_data.sample()
    canvas.itemconfig(word, text=sample['French'].item())
    timer = window.after(timer_ms, flip)


def flip():
    global timer
    reset_screen('English', e_img)
    canvas.itemconfig(word, text=sample['English'].item())
    timer = window.after(1200, wrong)


def reset_screen(lan, img):
    window.after_cancel(timer)
    canvas.itemconfig(canvas_img, image=img)
    canvas.itemconfig(lang, text=lan)


# --------------UI----------------
window = Tk()
window.title("Flash Card")
window.config(padx=40, pady=40, bg=BACKGROUND_COLOR)

canvas = Canvas(width=350, height=350, highlightthickness=0)
e_img = PhotoImage(file=E_IMG)
f_img = PhotoImage(file=F_IMG)
canvas_img = canvas.create_image(100, 120, image=f_img)
lang = canvas.create_text(170, 100, text='French', fill='black', font=('Aerial', 25, 'italic'))
word = canvas.create_text(170, 200, text=sample.French.values[0], fill='black', font=('Aerial', 45, 'bold'))
canvas.grid(row=0, column=0, columnspan=3, rowspan=3)

w_img = PhotoImage(file='./images/wrong.png')
w_button = Button(image=w_img, command=wrong, height=70, width=70)
w_button.grid(row=3, column=0, padx=50, pady=50)

r_img = PhotoImage(file='./images/right.png')
r_button = Button(image=r_img, command=right, height=70, width=70)
r_button.grid(row=3, column=2, padx=50, pady=50)

timer = window.after(timer_ms, flip)
window.mainloop()
