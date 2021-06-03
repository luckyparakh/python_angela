from API.TrueFalseGame.question_model import Question
from API.TrueFalseGame.data import tdb_question
from API.TrueFalseGame.quiz_brain import Quiz
from API.TrueFalseGame.ui import QuizInterface
from html import unescape

question_bank = []
for i, value in enumerate(tdb_question):
    ques_i = Question(text=unescape(value['question']), answer=value['correct_answer'])
    question_bank.append(ques_i)

quiz = Quiz(question_bank)
qi_obj = QuizInterface(quiz)

while quiz.still_has_question():
    quiz.next_question()

print(f"Quiz completes. Your final score is {quiz.score}/{quiz.question_number}.")
