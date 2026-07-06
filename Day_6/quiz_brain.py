from tabnanny import check


class QuizBrain:
    def __init__(self,question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0
    def any_questions_left(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        user_ans = input(f"Q.{self.question_number + 1} : {self.question_list[self.question_number].text}(True or False): ").lower()
        self.check_answer(user_ans,self.question_list[self.question_number].answer)
        self.question_number+=1
    def check_answer(self,user_answer,correct_answer):
        if user_answer == correct_answer.lower() :
            print("Correct Answer")
            self.score +=1
            print(f"Current Score is {self.score}")
        else:
            print("Wrong Ans")
            print(f"Correct answer is {correct_answer}")
            self.question_number = len(self.question_list)
