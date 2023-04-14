class QuizBrain:
    def __init__(self,qb_list):
        self.question_number = 0
        self.question_list = qb_list
        self.score = 0
        self.total = len(qb_list)

    def next_question(self):

        self.question_number +=1
        answer = input(f"Question {self.question_number}: {self.question_list[self.question_number].text}"
                       f" (True / False)?")

        self.check_answer(answer)

        #return self.question_list[self.question_number]['text']
        # self.question_number +=1


    def has_more_questions(self):
        # print(len(self.question_list))
        if self.question_number > len(self.question_list):
            return False
        else:
            return True

    def check_answer(self,qb_answer):
        if self.question_list[self.question_number].answer == qb_answer:
            print("Correct")
            self.score+=1
