from tkinter import Tk, Label, Button
from tkinter.filedialog import askopenfilename

class WCMenu:
    def __init__(self):
        self.win = Tk()
        self.win.title("Word Counter")

    def run(self):
        self.create_widgets()
        self.win.mainloop()

    def create_widgets(self):
        self.label = Label(
            self.win,
            text="Choose a file to count words"
        )
        self.label.pack()

        self.button = Button(
            self.win,
            text="Choose File",
            command=self.get_filepath
        )
        self.button.pack()

        self.error_message = Label(
            self.win,
            text=""
        )
        self.error_message.pack()

    def get_filepath(self):
        file_name = askopenfilename()

        try:
            chars, words, lines = wc(file_name)
            self.error_message.config(
                text=f"Characters: {chars}, Words: {words}, Lines: {lines}"
            )
        except FileNotFoundError:
            self.error_message.config(
                text="File not found"
            )
        except:
            self.error_message.config(
                text="An error occurred"
            )


def wc(filename):
    with open(filename, 'r') as f:
        text = f.read()
    number_of_characters = len(text)
    list_of_words = text.split()
    number_of_words = len(list_of_words)
    number_of_lines = text.count('\n')
    return number_of_characters, number_of_words, number_of_lines


def main():
    menu = WCMenu()
    menu.run()


main()
