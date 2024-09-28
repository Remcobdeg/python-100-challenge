from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

questions = []

for item in question_data:
    question = Question(item["question"], item["correct_answer"])
    questions.append(question)

quiz = QuizBrain(questions)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
# print(questions[1].question)