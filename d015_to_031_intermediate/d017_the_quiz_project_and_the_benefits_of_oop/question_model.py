# Set each Question as its own object following this class, with the given question text and correct answer.
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer