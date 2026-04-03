from pract5 import area_of_circle, circumference_of_circle

from tkinter import Tk, Frame, StringVar, DoubleVar, Label, Entry, Button

class CircleInfo:
    def __init__(self):
        self.win = Tk()
        self.win.title("Circle Information")
        self.win.geometry("250x100")

        self.main_frame = Frame(self.win)
        self.main_frame.grid(column=0, row=0)

        self.radius = DoubleVar()
        self.area = StringVar()
        self.circumference = StringVar()

        self.radius.set(0.0)
        self.area.set("Area:")
        self.circumference.set("Circumference:")

    def run(self):
        self.create_widgets()
        self.win.mainloop()

    def create_widgets(self):
        label_radius = Label(
            self.main_frame,
            text="Radius in cm:"
        )
        label_radius.grid(column=0, row=0)

        entry_radius = Entry(
            self.main_frame,
            textvariable=self.radius
        )
        entry_radius.grid(column=1, row=0)

        label_area = Label(
            self.main_frame,
            textvariable=self.area
        )
        label_area.grid(column=0, row=1)

        label_circumference = Label(
            self.main_frame,
            textvariable=self.circumference
        )
        label_circumference.grid(column=0, row=2)

        button_calculate = Button(
            self.main_frame,
            text="Calculate",
            command=self.calculate
        )
        button_calculate.grid(column=0, row=3)

        button_close = Button(
            self.main_frame,
            text="Close",
            command=self.win.destroy
        )
        button_close.grid(column=1, row=3)

    def calculate(self):
        radius = self.radius.get()
        area = area_of_circle(radius)
        circumference = circumference_of_circle(radius)
        self.area.set("Area: " + str(area) + " cm^2")
        self.circumference.set("Circumference: " + str(circumference) + " cm")


def main():
    app = CircleInfo()
    app.run()


if __name__ == "__main__":
    main()
