from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
Question_bank=[]
for i in range(len(question_data)):  
    q_i=Question(question_data[i]["text"],question_data[i]["answer"])
    Question_bank.append(q_i)
    
quiz=QuizBrain(Question_bank)
while quiz.still_has_question():
    quiz.next_question()
    print("your score",quiz.compteur )