from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
ticks = "✔"
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps, ticks
    reps = 1
    ticks = "✔"
    canvas.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    tick_label.config(text="")
    timer_label.config(text="Timer")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start():
    global reps, ticks
    if reps % 2 == 1:
        counter(WORK_MIN * 60)
        timer_label.config(text="Work")
        tick_label.config(text=ticks)
        ticks += "✔"
    else:
        if reps % 8 == 0:
            counter(LONG_BREAK_MIN * 60)
            timer_label.config(text="Break", fg=RED)
        else:
            counter(SHORT_BREAK_MIN * 60)
            timer_label.config(text="Break", fg=PINK)
    reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def counter(count):
    global timer
    if count > 0:
        count_min = int(count // 60)
        count_sec = count % 60
        if count_sec < 10:
            count_sec = f"0{count_sec}"
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
        timer = canvas.after(1000, counter, count - 1)
    if count == 0:
        start()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Labels
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
timer_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=240, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 110, image=tomato_img)
timer_text = canvas.create_text(100, 125, text='00:00', fill='white', font=(FONT_NAME, 30, 'bold'))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", highlightthickness=0, bg=YELLOW, command=start)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, bg=YELLOW, command=reset)
reset_button.grid(row=2, column=3)

tick_label = Label(fg=GREEN, bg=YELLOW)
tick_label.grid(row=3, column=1)

window.mainloop()
