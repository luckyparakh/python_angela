from tkinter import *

window = Tk()
window.title("Miles to KM converter")
window.config(padx=10, pady=10)

# Entries
miles_entry = Entry(width=5)
# Add some text to begin with
miles_entry.insert(END, string="0")
miles_entry.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

is_eq_to_label = Label(text="is equal to")
is_eq_to_label.grid(row=1, column=0)

kms_label = Label(text="0")
kms_label.grid(row=1, column=1)

km_label = Label(text="KM")
km_label.grid(row=1, column=2)


# Buttons
def action():
    miles = miles_entry.get()
    km = float(miles) * 1.689
    kms_label.config(text=f"{km:.2f}")


# calls action() when pressed
button = Button(text="Calculate", command=action)
button.grid(row=2, column=1)

window.mainloop()
