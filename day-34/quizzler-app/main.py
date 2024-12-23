from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import requests

# collect question data
try:
    response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
except requests.exceptions.RequestException as e:
    print(f"request error: {e}")
    print("\n USING STORED DATA FOR QUESTIONS")
    question_data = question_data
else:
    question_data = response.json()["results"]

# create the structure for the question bank
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
