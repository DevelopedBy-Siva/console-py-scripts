from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

questions = []
for qn in question_data:
    questions.append(Question(qn["text"], qn["answer"]))

quiz = QuizBrain(questions)
while quiz.still_has_questions():
    quiz.next_question()
    
print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")