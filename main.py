from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    """Create a list of questions and answers. """
    text = item["question"]
    answer = item["correct_answer"]
    question_bank.append(Question(text, answer))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print("Your final score was: {0}/{1}".format(quiz.score, quiz.question_number))
