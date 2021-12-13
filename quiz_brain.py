class QuizBrain:

    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def next_question(self):
        """Bring next question. """
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input("Q.{0}: {1} (True/False): ".format(self.question_number, current_question.text))
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        """Check if the questions are ended. """
        return self.question_number < len(self.questions_list)

    def check_answer(self, user_answer, correct_answer):
        """Check the user entered answer. """
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print("The correct answer was: {0}.".format(correct_answer))
        print("Your current score is {0}/{1}".format(self.score, self.question_number))
        print("\n")
