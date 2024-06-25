from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]
for question in question_data:
  question_text=question["text"]
  question_answer=question["answer"]
  my_ques=Question(question_text,question_answer)
  question_bank.append(my_ques)

Quiz=QuizBrain(question_bank)
while Quiz.still_has_questions()==True:
  Quiz.next_question()

print("You've completed the quiz")
print(f"Your final score is: {Quiz.score}/{Quiz.question_number}")
  



    