from tkinter import Tk, Frame, Entry, Button, Label, StringVar
from backend import Quiz


class QuizApp:

    def __init__(self, quiz):
        self.quiz = quiz

        self.win = Tk()
        self.win.title("Math Quiz")

        self.main_frame = Frame(self.win)
        self.main_frame.grid(row=0, column=0, padx=10, pady=10)

        self.new_question = StringVar()
        self.new_answer = StringVar()
        self.new_question.set("Enter question here")
        self.new_answer.set("Enter answer here")

        self.question_widgets = []

    def run(self):
        self.create_widgets()
        self.win.mainloop()

    def create_widgets(self):
        self.delete_all_question_widgets()

        question_entry = Entry(
            self.main_frame,
            textvariable=self.new_question,
            width=20
        )
        question_entry.grid(
            row=0,
            column=0,
            padx=5,
            pady=5
        )

        answer_entry = Entry(
            self.main_frame,
            textvariable=self.new_answer,
            width=20
        )
        answer_entry.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )

        add_question_button = Button(
            self.main_frame,
            text="Add",
            command=self.add_question
        )
        add_question_button.grid(
            row=0,
            column=2,
            padx=5,
            pady=5
        )

        num_questions = self.quiz.get_num_questions()

        for i in range(num_questions):
            question = self.quiz.get_question_at(i)

            question_label = Label(
                self.main_frame,
                text=question
            )
            question_label.grid(row=i+1, column=0)
            self.question_widgets.append(question_label)

            user_answer = Entry(self.main_frame)
            user_answer.grid(
                row=i+1,
                column=1,
                padx=5,
                pady=5
            )
            self.question_widgets.append(user_answer)

            check_answer_button = Button(
                self.main_frame,
                text="Check",
                command=lambda index=i, entry=user_answer: self.quiz.check_answer_at(index, entry)
            )
            check_answer_button.grid(
                row=i+1,
                column=2,
                padx=5,
                pady=5
            )
            self.question_widgets.append(check_answer_button)

            remove_question_button = Button(
                self.main_frame,
                text="Remove",
                command=lambda index=i: self.remove_question(index)
            )
            remove_question_button.grid(
                row=i+1,
                column=3,
                padx=5,
                pady=5
            )
            self.question_widgets.append(remove_question_button)

    def add_question(self):
        question = self.new_question.get()
        answer = self.new_answer.get()
        self.quiz.add_question(question, answer)

        self.new_question.set("Enter question here")
        self.new_answer.set("Enter answer here")
        self.create_widgets()

    def remove_question(self, index):
        self.quiz.remove_question_at(index)
        self.create_widgets()

    def delete_all_question_widgets(self):
        for widget in self.question_widgets:
            widget.destroy()
        self.question_widgets = []


def main():
    quiz = Quiz()
    quiz.add_question("What's 2+2?", "4")
    quiz.add_question("What's 3*3?", "9")

    app = QuizApp(quiz)
    app.run()


main()
