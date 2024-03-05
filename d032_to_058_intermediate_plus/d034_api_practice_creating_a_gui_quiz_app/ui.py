from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = 'Arial'


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        # Create the window and set it up with the title. Connect the UI to the Quiz Brain.
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, bg=THEME_COLOR)

        # Setting up the score label.
        self.lbl_score = Label(text='Score: 0', font=(FONT, 13, 'bold'), bg=THEME_COLOR, fg='#DDDDDD')
        self.lbl_score.grid(row=0, column=1, pady=(20, 0))

        # Setting up the canvas and the text to display questions.
        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text='TEST', font=(FONT, 20, 'italic'), fill='#555555', width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        # Setting up the True and False buttons.
        img_true = PhotoImage(file='images/true.png')
        img_false = PhotoImage(file='images/false.png')
        self.btn_true = Button(image=img_true, highlightthickness=0, command=self.true_pressed)
        self.btn_false = Button(image=img_false, highlightthickness=0, command=self.false_pressed)
        self.btn_true.grid(row=2, column=0, pady=(0, 20))
        self.btn_false.grid(row=2, column=1, pady=(0, 20))

        # Grabs the first question and begins the loop.
        self.get_next_question()
        self.window.mainloop()

    # Get the next question from the quiz brain, and print it to the canvas.
    def get_next_question(self):
        self.canvas.config(bg='White')
        if self.quiz.still_has_questions():
            self.lbl_score.config(text=f'Score: {self.quiz.score}/{self.quiz.question_number}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text='You\'ve reached the end of the quiz!')
            self.btn_true.config(state='disabled')
            self.btn_false.config(state='disabled')

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='Green')
        else:
            self.canvas.config(bg='Red')
        self.window.after(1000, self.get_next_question)