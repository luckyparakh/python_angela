class Quiz:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You are right!!")
        else:
            print("You are wrong.")
        print(f"Correct answer is {correct_answer.lower()}.")
        print(f"Current score is {self.score}/{self.question_number}")
        print("\n")

    def still_has_question(self):
        return len(self.question_list) > self.question_number

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question.text}? (True/False)")
        self.check_answer(user_answer, question.answer)

