from TrueFalseGame.question_model import Question
from TrueFalseGame.data import tdb_question
from TrueFalseGame.quiz_brain import Quiz
question_bank = []
for i, value in enumerate(tdb_question):
    ques_i = Question(text=value['question'], answer=value['correct_answer'])
    question_bank.append(ques_i)

quiz = Quiz(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print(f"Quiz completes. Your final score is {quiz.score}/{quiz.question_number}.")


