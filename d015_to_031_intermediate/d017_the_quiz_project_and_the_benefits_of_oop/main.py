from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

# Create an Question object in the new question bank for each element in the imported list. Dump that into a new Quiz Brain object.
question_bank = []
for i in question_data:
    question_bank.append(Question(i['text'], i['answer']))
quiz_brain = QuizBrain(question_bank)

# While there are still questions, ask more. Once the quiz brain is out of questions, display the final score.
while quiz_brain.still_has_questions():
    quiz_brain.next_question()
else:
    print(f'Thanks for playing the quiz game! Your final score is: {quiz_brain.score}/{quiz_brain.question_number}')