import pyfiglet
from time import sleep
result = pyfiglet.figlet_format("Quiz Time", font="ansi_shadow")

print(result)

from Day_6.quiz_brain import QuizBrain
from data import question_data
from question_model import Question
question_bank = []
for dictionary in question_data:
    question_bank.append(Question(dictionary["text"],dictionary["answer"]))
# for question in question_bank:
#     print(question.text,end=" : ")
#     print(question.answer)
quiz = QuizBrain(question_bank)
while quiz.any_questions_left():
    quiz.next_question()
