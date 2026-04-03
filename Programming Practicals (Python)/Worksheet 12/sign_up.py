from tkinter import Tk, Frame, StringVar, BooleanVar, Label, Entry, Button, Checkbutton

class SignUp:
    def __init__(self):
        self.win = Tk()
        self.win.title("Sign Up")
        self.win.geometry("250x150")

        self.main_frame = Frame(self.win)
        self.main_frame.grid(column=0, row=0)

        self.error_message = StringVar()
        self.error_message.set("")
        self.username = StringVar()
        self.username.set("")
        self.password = StringVar()
        self.password.set("")
        self.show_password = BooleanVar()
        self.show_password.set(False)

    def run(self):
        self.create_widgets()
        self.win.mainloop()

    def create_widgets(self):
        label_error_message = Label(
            self.main_frame,
            textvariable=self.error_message,
            width=30,
            fg="red"
        )
        label_error_message.grid(column=0, row=0, columnspan=2)

        label_username = Label(
            self.main_frame,
            text="Username:"
        )
        label_username.grid(column=0, row=1)

        entry_username = Entry(
            self.main_frame,
            width=25,
            textvariable=self.username
        )
        entry_username.grid(column=1, row=1)

        label_password = Label(
            self.main_frame,
            text="Password:"
        )
        label_password.grid(column=0, row=2)

        entry_password = Entry(
            self.main_frame,
            width=25,
            textvariable=self.password,
            show="*"
        )
        entry_password.grid(column=1, row=2)

        check_show_password = Checkbutton(
            self.main_frame,
            text="Show password",
            variable=self.show_password,
            command=self.toggle_show_password
        )
        check_show_password.grid(column=0, row=3, columnspan=2)

        button_sign_up = Button(
            self.main_frame,
            text="Sign Up",
            command=self.sign_up
        )
        button_sign_up.grid(column=0, row=4)

        button_cancel = Button(
            self.main_frame,
            text="Cancel",
            command=self.win.destroy
        )
        button_cancel.grid(column=1, row=4)

    def toggle_show_password(self):
        if self.show_password.get():
            show = ""
        else:
            show = "*"
        self.main_frame.children["!entry2"].config(show=show)

    def sign_up(self):
        username = self.username.get()
        password = self.password.get()

        if len(username) < 5:
            self.error_message.set("Username must be at least 5 characters.")
        elif len(password) < 8:
            self.error_message.set("Password must be at least 8 characters.")
        else:
            self.error_message.set("Sign up successful.")

            with open("user_data.csv", "a") as file:
                file.write(f"{username},{password}\n")


def main():
    app = SignUp()
    app.run()


if __name__ == "__main__":
    main()
