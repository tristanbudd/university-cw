from tkinter import Tk, Frame, DoubleVar, Label, Entry, Button

class TemperatureConverter:
    def __init__(self):
        self.win = Tk()
        self.win.title("Temperature Converter")
        self.win.geometry("230x100")

        self.main_frame = Frame(self.win)
        self.main_frame.grid(column=0, row=0)

        self.celsius = DoubleVar()
        self.celsius.set(0.0)
        self.fahrenheit = DoubleVar()
        self.fahrenheit.set(32.0)

    def run(self):
        self.create_widgets()
        self.win.mainloop()

    def create_widgets(self):
        label_celsius = Label(
            self.main_frame,
            text="Celsius:"
        )
        label_celsius.grid(column=0, row=0)

        entry_celsius = Entry(
            self.main_frame,
            textvariable=self.celsius
        )
        entry_celsius.grid(column=1, row=0)

        label_fahrenheit = Label(
            self.main_frame,
            text="Fahrenheit:"
        )
        label_fahrenheit.grid(column=0, row=1)

        entry_fahrenheit = Entry(
            self.main_frame,
            textvariable=self.fahrenheit
        )
        entry_fahrenheit.grid(column=1, row=1)

        button_celsius = Button(
            self.main_frame,
            text="Convert to Celsius",
            command=self.convert_to_celsius
        )
        button_celsius.grid(column=0, row=2)

        button_fahrenheit = Button(
            self.main_frame,
            text="Convert to Fahrenheit",
            command=self.convert_to_fahrenheit
        )
        button_fahrenheit.grid(column=1, row=2)

        button_close = Button(
            self.main_frame,
            text="Close",
            command=self.win.destroy
        )
        button_close.grid(column=0, row=3, columnspan=2)

    def convert_to_fahrenheit(self):
        celsius = self.celsius.get()
        fahrenheit = celsius * 9/5 + 32
        self.fahrenheit.set(fahrenheit)

    def convert_to_celsius(self):
        fahrenheit = self.fahrenheit.get()
        celsius = (fahrenheit - 32) * 5/9
        self.celsius.set(celsius)


def main():
    app = TemperatureConverter()
    app.run()


if __name__ == "__main__":
    main()
