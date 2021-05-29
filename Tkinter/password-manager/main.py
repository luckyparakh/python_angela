from tkinter import *
# Import * imports all Classes but messagebox is not class. Hence need to import it separately.
# To view this select messagebox line & right click -> Go to -> Implementation
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


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
    data_dict = {
        website: {
            'email': email,
            'password': password
        }
    }
    if len(website) == 0:
        messagebox.showerror('Error', 'Website is empty!')
    elif len(password) == 0:
        messagebox.showerror('Error', 'Password is empty!')
    else:
        try:
            with open('data.json', 'r') as file:
                # Reading Old Data
                json_data = json.load(file)
        except FileNotFoundError:
            with open('data.json', 'w') as file:
                # Writing data into file
                json.dump(data_dict, file, indent=4)
                messagebox.showinfo("Saved", "Password Saved!!")
        else:
            # Updating old data with new data
            json_data.update(data_dict)
            with open('data.json', 'w') as file:
                # Writing updated data into file
                json.dump(json_data, file, indent=4)
                messagebox.showinfo("Saved", "Password Saved!!")
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- Search------------------------------- #
def search():
    website = website_entry.get()
    try:
        with open('data.json', 'r') as data_file:
            data_dict = json.load(data_file)
            try:
                email = data_dict[website]['email']
                password = data_dict[website]['password']
                messagebox.showinfo(website, f"Email: {email}\nPassword: {password}")
            except KeyError as error_message:
                messagebox.showerror("Error", f"Key: {error_message} not found.")
    except FileNotFoundError:
        messagebox.showerror("Error", "No data file found.")


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

website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(row=1, column=1)

search_button = Button(text="Search", command=search, width=14)
search_button.grid(row=1, column=2)

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
