from tkinter import Tk, Frame, StringVar, BooleanVar, Label, Entry, Button

class TruthTable:
    def __init__(self):
        self.win = Tk()
        self.win.title("Truth Table")
        self.win.geometry("500x150")

        self.main_frame = Frame(self.win)
        self.main_frame.grid(column=0, row=0)

        for i in range(4):
            for j in range(4):
                variable_name = f"entry_{i}_{j}"
                setattr(self, variable_name, BooleanVar())
                getattr(self, variable_name).set(False)

        self.score = StringVar()
        self.score.set("Score: 0")

    def run(self):
        self.create_widgets()
        self.win.mainloop()

    def create_widgets(self):
        for i in range(4):
            for j in range(4):
                variable_name = f"entry_{i}_{j}"
                entry = Entry(
                    self.main_frame,
                    textvariable=getattr(self, variable_name)
                )
                entry.grid(column=j, row=i)

        label_score = Label(
            self.main_frame,
            textvariable=self.score
        )
        label_score.grid(column=0, row=4, columnspan=4)

        button_calculate = Button(
            self.main_frame,
            text="Calculate",
            command=self.calculate
        )
        button_calculate.grid(column=0, row=5, columnspan=4)

    def calculate(self):
        # OR Gate Truth Table
        correct_answers = [
            [False, True, True, True],
            [True, True, True, True],
            [True, True, True, True],
            [True, True, True, True]
        ]

        score = 0

        for i in range(4):
            for j in range(4):
                variable_name = f"entry_{i}_{j}"
                if getattr(self, variable_name).get() == correct_answers[i][j]:
                    score += 1

        self.score.set(f"Score: {score}")


def main():
    truth_table = TruthTable()
    truth_table.run()


if __name__ == "__main__":
    main()