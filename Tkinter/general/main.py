import tkinter

window = tkinter.Tk()
window.title("First")

label = tkinter.Label(text="I am label")
label.grid(column=0, row=0)


def bclick():
    ip = input.get()
    label.config(text=ip)

button1 = tkinter.Button(text="Button1", command=bclick)
button1['text'] = 'Click'
button1.config(text='Click!!')
button1.grid(column=2, row=0)

button = tkinter.Button(text="Click Me", command=bclick)
button['text'] = 'Click'
button.config(text='Click!!')
button.grid(column=1, row=1)

inp = tkinter.Entry(textvariable='Name')
inp.grid(column=3, row=3)

window.mainloop()
