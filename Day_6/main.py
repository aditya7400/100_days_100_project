import pyfiglet
result = pyfiglet.figlet_format("Quiz Time", font="ansi_shadow")

print(result)

from Day_6.quiz_brain import QuizBrain
from data import question_data
from question_model import Question
question_bank = []
for dictionary in question_data["results"]:
    question = dictionary["question"]
    answer = dictionary["correct_answer"]
    question_bank.append(Question(text=question,answer=answer))

quiz = QuizBrain(question_bank)
while quiz.any_questions_left():
    quiz.next_question()
