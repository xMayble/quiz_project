from question_model import Question
from data import question_data

question_bank = []

for dict in question_data:
    q = dict['text']
    a = dict['answer']
    new_question = Question(q, a)
    question_bank.append(new_question)

print(question_bank)