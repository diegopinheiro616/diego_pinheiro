"""
Day 17 - How to create your own Class in Python
"""
# ################  Creating a Class in Python ####################
"""
# Pascalcase(Class) / camelCase(none) / snake_case(all rest)
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0  # <---- Como deu um valor inicial não necessita especificar dentro dos parenteses.

user_1 = User("001", "Angela")
# print(user_1.followers)
# user_2 = User("002", "Jack")
"""
# ################ Adding Methods to Class ####################
"""
# Class Car:
    # def enter_race_mode():
        # self.seats = 2
# my_car.enter_race_mode()
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "Angela")
user_2 = User("002", "Jack")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
"""
# ################ Quiz Project ####################
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You've completed the Quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}.")





