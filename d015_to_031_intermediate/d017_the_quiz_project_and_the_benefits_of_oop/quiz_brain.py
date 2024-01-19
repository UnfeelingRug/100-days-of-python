class QuizBrain:
    # Initialize self with the given question list, resetting score and question number to zero.
    def __init__(self, questions_list):
        self.questions_list = questions_list
        self.question_number = 0
        self.score = 0

    # Fetch the next question, ask it, and check the user's input for the correct answer.
    def next_question(self):
        question = self.questions_list[self.question_number]
        self.question_number += 1
        guess = input(f'Q{self.question_number}. {question.text} True or False? ').upper()
        self.check_answer(guess, question.answer.upper())

    # Determine if there are still questions remaining.
    def still_has_questions(self):
        return self.question_number < len(self.questions_list)
    
    # Check if the answer is correct, and increase the score if it is.
    # Check exact matches, or T/F for True/False. Not case-sensitive.
    def check_answer(self, guess, answer):
        if guess == answer \
        or (guess == 'T' and answer == "TRUE") \
        or (guess == 'F' and answer == 'FALSE'):
            self.score += 1
            print(f'Correct, you get a point!')
        else:
            print(f'Ooh, too bad! We were looking for "{answer}" for this one...')
        print(f'Current score: {self.score}/{self.question_number}\n')