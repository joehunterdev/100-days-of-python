import data
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from pprint import pprint
from inspect import getmembers
# TODO 1. Question class
# TODO 2. init method
# TODO 3. Two atts (text answer) init whn object created

# TODO 5. Import question model data as ques obj
# TODO 4. Move class to separate file
# TODO 6. Meet desired initialization

q = data.question_data

# Initialization
# q1= Question("2+3=5",'True')
# question_bank=[
#       Question(q[0]["text"],q[0]["answer"]),
#       Question(q[1]["text"], q[1]["answer"]),
#       Question(q[2]["text"], q[1]["answer"]),
# ]

#print(data.question_data[0]["text"],data.question_data[0]["answer"])

question_bank = []

for question in question_data["results"]:
    # print(question["correct_answer"])
    question_bank.append(Question(question["question"],question["correct_answer"]))

# print(question_bank)
# TODO 7. Retrieve item at current position:
# TODO 7. Use input to show question text and ask for answer
# pprint(getmembers(question_bank[0].answer))
# print(question_bank[0]['text'])
qb = QuizBrain(question_bank)
# qb.next_question()

# TODO 8. Loop throguh questions
# TODO 10. Check answer


while qb.has_more_questions() == True:
    print(f"Score is {qb.score} / {qb.total} ")
    qb.next_question()
    continue

