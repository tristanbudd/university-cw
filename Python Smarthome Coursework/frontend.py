from tkinter import Tk, Frame, Label, Button, Entry, OptionMenu, messagebox, StringVar, filedialog
from backend import SmartPlug, SmartFridge, SmartTV, SmartHome
from json import loads, dumps

# --------------- Task #4 & #5 - SmartHomeApp Class (Tkinter) ---------------
class SmartHomeApp:
    def __init__(self, smart_home):
        self.smart_home = smart_home or SmartHome(5)
        self.win = Tk()
        self.win.title("Smart Home App")
        self.win.resizable(False, False)

        self.main_frame = Frame(self.win)
        self.main_frame.grid(row=0, column=0, padx=10, pady=10)

        self.widgets = []

    def run(self):
        self.create_widgets()
        self.win.mainloop()

    def create_widgets(self):
        turn_on_all_button = Button(
            self.main_frame,
            text="Turn On All",
            command=self.switch_all_on
        )
        turn_on_all_button.grid(row=0, column=0, columnspan=3, padx=5, pady=5)
        self.widgets.append(turn_on_all_button)

        turn_off_all_button = Button(
            self.main_frame,
            text="Turn Off All",
            command=self.switch_all_off
        )
        turn_off_all_button.grid(row=0, column=3, columnspan=3, padx=5, pady=5)
        self.widgets.append(turn_off_all_button)

        for i, device in enumerate(self.smart_home.devices):
            device_frame = Frame(self.main_frame)
            device_frame.grid(row=i + 1, column=0, columnspan=6, padx=5, pady=5)
            self.widgets.append(device_frame)

            if isinstance(device, SmartPlug):
                device_info = f"Plug: {('On' if device.switched_on else 'Off')}, Consumption Rate: {device.consumption_rate}"
            elif isinstance(device, SmartFridge):
                device_info = f"Fridge: {('On' if device.switched_on else 'Off')}, Temperature: {device.temperature}°C"
            elif isinstance(device, SmartTV):
                device_info = f"TV: {('On' if device.switched_on else 'Off')}, Channel: {device.channel}"
            else:
                device_info = "Unknown Device"

            device_label = Label(
                device_frame,
                text=device_info
            )
            device_label.grid(row=0, column=0, columnspan=3)
            self.widgets.append(device_label)

            toggle_button = Button(
                device_frame,
                text="Toggle",
                command=lambda i=i: self.toggle_device(i)
            )
            toggle_button.grid(row=0, column=3, columnspan=2, padx=5)
            self.widgets.append(toggle_button)

            edit_button = Button(
                device_frame,
                text="Edit",
                command=lambda i=i: self.edit_device(i)
            )
            edit_button.grid(row=0, column=5, columnspan=1, padx=5)
            self.widgets.append(edit_button)

            delete_button = Button(
                device_frame,
                text="Delete",
                command=lambda i=i: self.delete_device(i)
            )
            delete_button.grid(row=0, column=6, columnspan=2, padx=5)
            self.widgets.append(delete_button)

        add_button = Button(
            self.main_frame,
            text="Add Device",
            command=self.add_device
        )
        add_button.grid(row=len(self.smart_home.devices) + 1, column=0, columnspan=6, padx=5, pady=5)
        self.widgets.append(add_button)

    def refresh_widgets(self):
        for widget in self.widgets:
            widget.destroy()
        self.widgets = []

        self.create_widgets()

    def switch_all_on(self):
        self.smart_home.switch_all_on()
        self.refresh_widgets()

    def switch_all_off(self):
        self.smart_home.switch_all_off()
        self.refresh_widgets()

    def toggle_device(self, index):
        try:
            self.smart_home.toggle_device(index)
        except ValueError as error:
            print(error)
        self.refresh_widgets()

    def edit_device(self, index):
        device = self.smart_home.get_device(index)
        edit_window = Tk()
        edit_window.title("Edit Device")
        edit_window.resizable(False, False)

        device_label = Label(
            edit_window,
            text=device
        )

        device_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        attribute_label = Label(
            edit_window,
            text="Attribute:"
        )
        attribute_label.grid(row=1, column=0, padx=5, pady=5)

        attribute_entry = Entry(edit_window)
        attribute_entry.grid(row=1, column=1, padx=5, pady=5)

        def update_device():
            if attribute_entry.get().isdigit():
                attribute_value = int(attribute_entry.get())

                try:
                    self.smart_home.update_option(index, attribute_value)
                except ValueError as error:
                    error_message_label.config(text=str(error))
                    return
            else:
                error_message_label.config(text="Attribute must be a positive full number!")
                return

            edit_window.destroy()
            self.refresh_widgets()

        select_button = Button(
            edit_window,
            text="Update Device",
            command=update_device
        )
        select_button.grid(row=2, column=0, padx=5, pady=5)

        cancel_button = Button(
            edit_window,
            text="Cancel",
            command=edit_window.destroy
        )
        cancel_button.grid(row=2, column=1, padx=5, pady=5)

        error_message_label = Label(
            edit_window,
            text="",
            fg="red"
        )
        error_message_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        edit_window.mainloop()

    def delete_device(self, index):
        confirm = messagebox.askyesno("Delete Device", "Are you sure you want to delete this device?")

        if confirm:
            self.smart_home.remove_device(index)
            self.refresh_widgets()

    def add_device(self):
        add_window = Tk()
        add_window.title("Add Device")
        add_window.resizable(False, False)

        device_type_label = Label(
            add_window,
            text="Device Type:"
        )
        device_type_label.grid(row=0, column=0, padx=5, pady=5)

        device_type_var = StringVar(add_window)
        device_type_var.set("Smart Plug")

        device_type_option = OptionMenu(
            add_window,
            device_type_var,
            "Smart Plug",
            "Smart Fridge",
            "Smart TV"
        )
        device_type_option.grid(row=0, column=1, padx=5, pady=5)

        attribute_label = Label(
            add_window,
            text="Attribute (Optional):"
        )
        attribute_label.grid(row=1, column=0, padx=5, pady=5)

        attribute_entry = Entry(add_window)
        attribute_entry.grid(row=1, column=1, padx=5, pady=5)

        def create_device():
            item_type = device_type_var.get()
            try:
                if attribute_entry.get() != "" and not attribute_entry.get().isdigit():
                    raise ValueError("Attribute must be a positive number!")

                if attribute_entry.get().isdigit():
                    attribute_value = int(attribute_entry.get())
                else:
                    attribute_value = None

                device_classes = {
                    "Smart Plug": SmartPlug,
                    "Smart Fridge": SmartFridge,
                    "Smart TV": SmartTV
                }

                device_class = device_classes.get(item_type)
                if device_class:
                    if attribute_value is not None:
                        device = device_class(attribute_value)
                    else:
                        device = device_class()
                    self.smart_home.add_device(device)
                else:
                    return
            except ValueError as error:
                error_message_label.config(text=str(error))
                return

            add_window.destroy()
            self.refresh_widgets()

        select_button = Button(
            add_window,
            text="Add Device",
            command=create_device
        )
        select_button.grid(row=2, column=0, padx=5, pady=5)

        cancel_button = Button(
            add_window,
            text="Cancel",
            command=add_window.destroy
        )
        cancel_button.grid(row=2, column=1, padx=5, pady=5)

        error_message_label = Label(
            add_window,
            text="",
            fg="red"
        )
        error_message_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        add_window.mainloop()


def test_smart_home_system():
    # Task #4 & #5 - Test SmartHomeApp Class
    print("--------------- Task #4 - Smart Home App Test ---------------")
    smart_home = SmartHome(5)
    smart_plug = SmartPlug()
    smart_fridge = SmartFridge()
    smart_tv = SmartTV()
    smart_home.add_device(smart_plug)
    smart_home.add_device(smart_fridge)
    smart_home.add_device(smart_tv)
    smart_home_app = SmartHomeApp(smart_home)
    smart_home_app.run()


# --------------- Challenge Task ---------------
class SmartHomesApp:
    def __init__(self):
        self.smart_homes = []

        self.win = Tk()
        self.win.title("Smart Homes App")
        self.win.resizable(False, False)

        self.main_frame = Frame(self.win)
        self.main_frame.grid(row=0, column=0, padx=10, pady=10)

        self.widgets = []

    def run(self):
        self.create_widgets()
        self.win.mainloop()

    def create_widgets(self):
        for i, smart_home in enumerate(self.smart_homes):
            smart_home_frame = Frame(self.main_frame)
            smart_home_frame.grid(row=i + 1, column=0, columnspan=3, padx=5, pady=5)
            self.widgets.append(smart_home_frame)

            device_on_count = 0

            for device in smart_home.devices:
                if device.switched_on:
                    device_on_count += 1

            smart_home_label = Label(
                smart_home_frame,
                text=f"Smart Home #{i + 1}\n{len(smart_home.devices)} device(s)\n{device_on_count} device(s) on"
            )
            smart_home_label.grid(row=0, column=0, padx=5, pady=5)
            self.widgets.append(smart_home_label)

            view_button = Button(
                smart_home_frame,
                text="View",
                command=lambda i=i: self.view_smart_home(i)
            )
            view_button.grid(row=0, column=1, padx=5, pady=5)
            self.widgets.append(view_button)

            delete_button = Button(
                smart_home_frame,
                text="Delete",
                command=lambda i=i: self.delete_smart_home(i)
            )
            delete_button.grid(row=0, column=2, padx=5, pady=5)
            self.widgets.append(delete_button)

        add_button = Button(
            self.main_frame,
            text="Add Smart Home",
            command=self.add_smart_home
        )
        add_button.grid(row=len(self.smart_homes) + 1, column=0, padx=5, pady=5)
        self.widgets.append(add_button)

        refresh_button = Button(
            self.main_frame,
            text="Refresh",
            command=self.refresh_widgets
        )
        refresh_button.grid(row=len(self.smart_homes) + 1, column=1, padx=5, pady=5)
        self.widgets.append(refresh_button)

        open_save_button = Button(
            self.main_frame,
            text="Open Save",
            command=self.open_save
        )
        open_save_button.grid(row=len(self.smart_homes) + 2, column=0, padx=5, pady=5)
        self.widgets.append(open_save_button)

        save_current_button = Button(
            self.main_frame,
            text="Save Current",
            command=self.save_current
        )
        save_current_button.grid(row=len(self.smart_homes) + 2, column=1, padx=5, pady=5)
        self.widgets.append(save_current_button)

    def refresh_widgets(self):
        for widget in self.widgets:
            widget.destroy()
        self.widgets = []

        self.create_widgets()

    def add_smart_home(self):
        smart_home = SmartHome(5)
        self.smart_homes.append(smart_home)
        self.refresh_widgets()

    def view_smart_home(self, index):
        smart_home = self.smart_homes[index]
        smart_home_app = SmartHomeApp(smart_home)
        smart_home_app.run()

    def delete_smart_home(self, index):
        confirm = messagebox.askyesno("Delete Smart Home", "Are you sure you want to delete this smart home?")

        if confirm:
            self.smart_homes.pop(index)
            self.refresh_widgets()

    def open_save(self):
        file_path = filedialog.askopenfilename(filetypes=[("Smart Home Data", "*.json")])

        if file_path:
            try:
                with open(file_path, "r") as file:
                    raw_data = file.read()
                    data = loads(raw_data)

                    self.smart_homes = []

                    for smart_home_data in data["smart_homes"]:
                        smart_home = SmartHome(5)
                        self.smart_homes.append(smart_home)

                        for device_data in smart_home_data["devices"]:
                            device_classes = {
                                "SmartPlug": SmartPlug,
                                "SmartFridge": SmartFridge,
                                "SmartTV": SmartTV
                            }

                            device_class = device_classes.get(device_data["type"])
                            if device_class:
                                device = device_class(device_data["attribute"])
                                device.switched_on = device_data["switched_on"]
                                smart_home.add_device(device)

                self.refresh_widgets()

                messagebox.showinfo("Open Successful", "Smart Home data loaded successfully!")
            except FileNotFoundError:
                messagebox.showerror("File Not Found", "File not found!")
            except Exception as error:
                messagebox.showerror("Error", f"An error occurred: {error}")

    def save_current(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("Smart Home Data", "*.json")])

        if file_path:
            with open(file_path, "w") as file:
                raw_data = {
                    "smart_homes": [
                        {
                            "devices": [
                                {
                                    "type": type(device).__name__,
                                    "switched_on": device.switched_on,
                                    "attribute": device.get_attribute()
                                }
                                for device in smart_home.devices
                            ]
                        }
                        for smart_home in self.smart_homes
                    ]
                }

                data = dumps(raw_data, indent=4)
                file.write(data)

            messagebox.showinfo("Save Successful", "Smart Home data saved successfully!")


def test_smart_homes_app():
    # Challenge Task - Test SmartHomesApp Class
    print("--------------- Challenge Task - Smart Homes Control Hub ---------------")
    smart_homes_app = SmartHomesApp()
    smart_homes_app.run()


if __name__ == "__main__":
    # test_smart_home_system()
    test_smart_homes_app()
