import tkinter as tk
import os
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
THEME_FONT = 'Arial'

app_path = os.path.dirname(__file__)

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):

        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.card = tk.Canvas(width=300, height=250, background="white")
        self.card_text = self.card.create_text(
            150,
            125, 
            width=280,
            text='quiz', 
            font=(THEME_FONT, 20, "italic"), 
            fill="black"
        )
        self.card.grid(column=1,row=2,columnspan = 2, pady=50)

        self.score_count = tk.Label(text="Score: 0", font=(THEME_FONT, 10, "bold"), bg=THEME_COLOR, fg="white")
        self.score_count.grid(column=2, row=1)

        false_image = tk.PhotoImage(file = os.path.join(app_path,'images/false.png'))
        self.false_button = tk.Button(image=false_image, highlightthickness=0, bd=0, command=self.is_false)
        self.false_button.grid(column=2, row=3)

        true_image = tk.PhotoImage(file = os.path.join(app_path,'images/true.png'))
        self.true_button = tk.Button(image=true_image, highlightthickness=0, bd=0, command=self.is_true)
        self.true_button.grid(column=1, row=3)

        # start the quiz
        self.get_next_question()

        self.window.mainloop()

    def is_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def is_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.card.config(bg="green")
        else:
            self.card.config(bg="red")
        self.window.after(1000, self.get_next_question)

    def get_next_question(self):
        self.card.config(bg="white")
        if self.quiz.still_has_questions(): 
            self.score_count.config(text=f"Score: {self.quiz.score}")
            question_text = self.quiz.next_question()
            self.card.itemconfig(self.card_text, text=question_text)
        else:
            self.card.itemconfig(self.card_text, text="You've completed the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")



