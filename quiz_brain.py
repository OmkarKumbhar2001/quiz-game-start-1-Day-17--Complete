class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_question(self):
        return len(self.question_list) > self.question_number

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        userInput = input(
            f"Q{self.question_number} {current_question.text}(True/False): ")
        self.check_answer(userInput, current_question)

    def check_answer(self, userInput, current_question):
        if userInput.lower() == current_question.answer.lower():
            self.score += 1
            print("Nice Correct Answer")
        else:
            print("Ohh o Wrong Answer")
        print(f"Your Current Score is: {self.score}/{self.question_number}")
        print(f"Correct Answer is : {current_question.answer}")
        print()
