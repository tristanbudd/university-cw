from tkinter import Tk, Frame, Entry, Button, Label, StringVar, Toplevel
from backend import Task, TaskList

class TodoListApp:

    def __init__(self, task_list):
        self.task_list = task_list

        self.win = Tk()
        self.win.title("Todo List")

        self.main_frame = Frame(self.win)
        self.main_frame.grid(row=0, column=0, padx=10, pady=10)

        self.new_task = StringVar()
        self.new_task.set("Enter task here")

        self.task_widgets = []

    def run(self):
        self.create_widgets()
        self.win.mainloop()

    def create_widgets(self):
        self.delete_all_task_widgets()

        task_entry = Entry(
            self.main_frame,
            textvariable=self.new_task,
            width=20
        )
        task_entry.grid(
            row=0,
            column=0,
            padx=5,
            pady=5
        )

        add_task_button = Button(
            self.main_frame,
            text="Confirm",
            command=self.add_task
        )
        add_task_button.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )

        for i in range(self.task_list.get_num_tasks()):
            task_message = self.task_list.get_task_message_by_index(i)

            task_label = Label(
                self.main_frame,
                text=task_message
            )
            task_label.grid(
                row=i + 1,
                column=0,
                padx=5,
                pady=5
            )

            edit_button = Button(
                self.main_frame,
                text="Edit",
                command=lambda i=i: self.open_edit_window(i)
            )
            edit_button.grid(
                row=i + 1,
                column=1,
                padx=5,
                pady=5
            )

            remove_button = Button(
                self.main_frame,
                text="Remove",
                command=lambda i=i: self.remove_task(i)
            )
            remove_button.grid(
                row=i + 1,
                column=2,
                padx=5,
                pady=5
            )

            self.task_widgets.append((task_label, edit_button, remove_button))

    def delete_all_task_widgets(self):
        for task_widget in self.task_widgets:
            for widget in task_widget:
                widget.destroy()
        self.task_widgets = []

    def add_task(self):
        self.task_list.create_new_task(self.new_task.get())
        self.create_widgets()

    def open_edit_window(self, edit_index):
        edit_window = Toplevel(self.win)
        edit_window.title("Edit Task")

        edit_entry = Entry(
            edit_window,
            width=20
        )
        edit_entry.grid(
            row=0,
            column=0,
            padx=5,
            pady=5
        )

        confirm_button = Button(
            edit_window,
            text="Confirm",
            command=lambda: [self.edit_task(edit_index, edit_entry.get()), edit_window.destroy()]
        )
        confirm_button.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )

    def edit_task(self, index, new_message):
        self.task_list.set_task_message_at_index(index, new_message)
        self.create_widgets()

    def remove_task(self, index):
        self.task_list.remove_task_at_index(index)
        self.create_widgets()


def main():
    task_list = TaskList()
    app = TodoListApp(task_list)
    app.run()

if __name__ == "__main__":
    main()

