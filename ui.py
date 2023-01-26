from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.configure(bg=THEME_COLOR)

        # Labels
        self.score_label = Label(
            text="Score 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1, padx=20, pady=20)

        # Canvas
        self.my_canvas = Canvas(self.window, bg="white", height=250, width=300)
        self.questionText = self.my_canvas.create_text(
            150, 125, text="Question", font=('Arial', 20, 'italic'), width=280)
        self.my_canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        # Buttons
        self.trueImage = PhotoImage(file='./images/true.png')
        self.falseImage = PhotoImage(file='./images/false.png')
        self.trueButton = Button(image=self.trueImage, command=self.ClickTrueAnswer
                                 )
        self.trueButton.grid(row=2, column=0, pady=20)
        self.falseButton = Button(
            image=self.falseImage, command=self.ClickFalseAnswer)
        self.falseButton.grid(row=2, column=1, pady=20, )

        self.GetNextQuestion()
        # start window
        self.window.mainloop()

    def GetNextQuestion(self):
        if self.quiz.still_has_questions():
            self.my_canvas.config(bg="white")
            nextQuestionText = self.quiz.next_question()
            self.my_canvas.itemconfig(self.questionText, text=nextQuestionText)
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.falseButton.config(state="disabled")
            self.trueButton.config(state="disabled")
            self.my_canvas.itemconfig(self.questionText, text="GAME OVER")

    def ClickTrueAnswer(self):
        is_answer_right = self.quiz.check_answer("True")
        self.GiveFeedback(is_answer_right)

    def ClickFalseAnswer(self):
        is_answer_right = self.quiz.check_answer("False")
        self.GiveFeedback(is_answer_right)

    def GiveFeedback(self, is_answer_right: bool):
        if is_answer_right:
            self.my_canvas.config(bg="green")
        else:
            self.my_canvas.config(bg="red")

        self.window.after(1000, self.GetNextQuestion)
