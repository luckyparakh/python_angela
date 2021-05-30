import requests
from tkinter import *



def quote():
    response = requests.get('https://api.kanye.rest/')
    response.raise_for_status()
    data = response.json()['quote'].strip()
    canvas.itemconfig(quote_text, text=data)


###############UI####################
window = Tk()
window.title("Quotes")
window.config(padx=30, pady=30)

canvas = Canvas(width=400, height=200, highlightthickness=0, bg='cyan')
# bg_img = PhotoImage(file='./images/background.png')
# canvas.create_image(bg_img)
canvas.grid(row=0, column=0, columnspan=3)

canvas.create_text(200, 20, text='Quote', fill='black', font=('Aerial', 25, 'italic'))
quote_text = canvas.create_text(100, 100, text='Quote', width=200, font=('Aerial', 10))

k_button = Button(bg='yellow', command=quote, text='Quote')
k_button.grid(row=1, column=1, padx=10, pady=10)
k_button.invoke()

window.mainloop()
