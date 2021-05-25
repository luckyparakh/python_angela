from tkinter import *
# Import * imports all Classes but messagebox is not class. Hence need to import it separately.
# To view this select messagebox line & right click -> Go to -> Implementation
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_list = []

    password_letter = [choice(letters) for _ in range(randint(6, 10))]
    password_symbol = [choice(letters) for _ in range(randint(1, 2))]
    password_number = [choice(letters) for _ in range(randint(1, 4))]
    password_list = password_letter + password_number + password_symbol

    shuffle(password_list)
    random_password = "".join(password_list)
    password_entry.insert(0, random_password)
    pyperclip.copy(random_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website) == 0:
        messagebox.showerror('Error', 'Website is empty!')
    elif len(password) == 0:
        messagebox.showerror('Error', 'Password is empty!')
    else:
        detail = f"{website} | {email} | {password}"
        with open('details.text', 'a') as file:
            file.write(detail + "\n")
        messagebox.showinfo("Saved", "Password Saved!!")
        website_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)
canvas = Canvas(width=210, height=250)
my_img = PhotoImage(file="lock.png")
canvas.create_image(100, 120, image=my_img)
canvas.grid(row=0, column=1, columnspan=3)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=41)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_entry = Entry(width=41)
email_entry.insert(0, string="luckyparakh@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

gpassword_button = Button(text="Generate Password", command=generate_password)
gpassword_button.grid(row=3, column=2)

add_button = Button(text="Add", command=save_password, width=35)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
