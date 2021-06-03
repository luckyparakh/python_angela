THEME_COLOR = '#375362'
from tkinter import *
from API.TrueFalseGame.quiz_brain import Quiz


class QuizInterface:

    def __init__(self, ques_brain: Quiz):
        self.quiz = ques_brain
        self.window = Tk()
        self.window.title('Quiz')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text=f"Score:{self.quiz.score}", fg=THEME_COLOR)
        self.score_label.grid(row=0, column=1, padx=20, pady=20)
        self.canvas = Canvas(width=300, height=300, highlightthickness=0, bg='white')
        self.question_text = self.canvas.create_text(150, 100,
                                                     text='Some Text',
                                                     font=('Aerial', 20, 'italic'),
                                                     width=280)
        self.canvas.grid(row=1, column=0, columnspan=2)
        r_img = PhotoImage(file='images/right.png')
        self.r_button = Button(image=r_img, height=70, width=70, highlightthickness=0, command=self.true_pressed)
        self.r_button.grid(row=2, column=0, padx=20, pady=20)
        w_img = PhotoImage(file='images/wrong.png')
        self.w_button = Button(image=w_img, height=70, width=70, highlightthickness=0, command=self.false_pressed)
        self.w_button.grid(row=2, column=1, padx=20, pady=20)
        self.get_next_question()
        self.window.mainloop()

    def true_pressed(self):
        self.feedback(self.quiz.check_answer('True'))

    def false_pressed(self):
        self.feedback(self.quiz.check_answer('False'))

    def get_next_question(self):
        self.canvas.config(bg='white')
        print(self.quiz.question_number)
        if self.quiz.still_has_question():
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question)
        else:
            self.canvas.itemconfig(self.question_text, text="Quiz Ends!!")
            self.w_button.config(state='disabled')
            self.r_button.config(state='disabled')

    def feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg='green')
            self.score_label.config(text=f"Score:{self.quiz.score}")
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
