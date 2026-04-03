from tkinter import Tk, Frame, StringVar, DoubleVar, Label, Entry, Button

class WhatToDoToday:
    def __init__(self):
        self.win = Tk()
        self.win.title("What to do today?")
        self.win.geometry("300x100")

        self.main_frame = Frame(self.win)
        self.main_frame.grid(column=0, row=0)

        self.temperature = DoubleVar()
        self.temperature.set(0.0)
        self.activity = StringVar()
        self.activity.set("")

    def run(self):
        self.create_widgets()
        self.win.mainloop()

    def create_widgets(self):
        label_temperature = Label(
            self.main_frame,
            text="Temperature in Celsius:"
        )
        label_temperature.grid(column=0, row=0)

        entry_temperature = Entry(
            self.main_frame,
            textvariable=self.temperature
        )
        entry_temperature.grid(column=1, row=0)

        label_activity = Label(
            self.main_frame,
            text="Activity:"
        )
        label_activity.grid(column=0, row=1)

        label_activity = Label(
            self.main_frame,
            textvariable=self.activity
        )
        label_activity.grid(column=1, row=1)

        button_decide = Button(
            self.main_frame,
            text="Decide",
            command=self.decide
        )
        button_decide.grid(column=0, row=2, columnspan=2)

    def decide(self):
        temperature = self.temperature.get()

        if temperature > 25:
            self.activity.set("Swim in the sea.")
        elif temperature <= 10:
            self.activity.set("Shop at Gunwharf Quays.")
        else:
            self.activity.set("Watch a film at home.")


def main():
    app = WhatToDoToday()
    app.run()


if __name__ == "__main__":
    main()
