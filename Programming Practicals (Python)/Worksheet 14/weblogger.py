from tkinter import Tk, Frame, Label, Entry, Button, messagebox
import random

class WeatherLogger:
    def __init__(self):
        self.win = Tk()
        self.win.title("Weather Logger")

        self.main_frame = Frame(self.win)
        self.main_frame.grid(row=0, column=0, padx=10, pady=10)

        self.seasons = {
            "Spring": {"min": 0, "max": 0},
            "Summer": {"min": 0, "max": 0},
            "Autumn": {"min": 0, "max": 0},
            "Winter": {"min": 0, "max": 0}
        }

    def run(self):
        self.create_widgets()
        self.win.mainloop()

    def create_widgets(self):
        info_label = Label(
            self.main_frame,
            text="Enter the weather data for each season here:"
        )
        info_label.grid(row=0, column=0, columnspan=2, pady=10)

        for i, season in enumerate(self.seasons):
            season_label = Label(
                self.main_frame,
                text=season
            )
            season_label.grid(row=i+1, column=0, padx=10, pady=10)

            min_label = Label(
                self.main_frame,
                text="Min:"
            )
            min_label.grid(row=i+1, column=1, padx=10, pady=10)

            min_entry = Entry(self.main_frame)
            min_entry.grid(row=i+1, column=2, padx=10, pady=10)

            max_label = Label(
                self.main_frame,
                text="Max:"
            )
            max_label.grid(row=i+1, column=3, padx=10, pady=10)

            max_entry = Entry(self.main_frame)
            max_entry.grid(row=i+1, column=4, padx=10, pady=10)

            self.seasons[season]["min"] = min_entry
            self.seasons[season]["max"] = max_entry

        submit_button = Button(
            self.main_frame,
            text="Submit",
            command=self.submit
        )
        submit_button.grid(row=5, column=0, columnspan=5, pady=10)

        error_message = Label(
            self.main_frame,
            text="",
            fg="red"
        )
        error_message.grid(row=6, column=0, columnspan=5)

    def submit(self):
        for season in self.seasons:
            min_temp = self.seasons[season]["min"].get()
            max_temp = self.seasons[season]["max"].get()

            if not min_temp or not max_temp:
                messagebox.showerror(
                    "Error",
                    "Please fill in all fields."
                )
                return

            try:
                min_temp = float(min_temp)
                max_temp = float(max_temp)
            except ValueError:
                messagebox.showerror(
                    "Error",
                    "Please enter valid numbers."
                )
                return

            if min_temp > max_temp:
                messagebox.showerror(
                    "Error",
                    "The minimum temperature must be less than the maximum temperature."
                )
                return

            self.seasons[season]["min"] = min_temp
            self.seasons[season]["max"] = max_temp

        csv_array = []

        for i in self.seasons:
            for j in range(90):
                for k in range(24):
                    random_temperature = random.uniform(self.seasons[i]["min"], self.seasons[i]["max"])
                    random_temperature = f"{random_temperature:.2f}"
                    csv_array.append(f"{i},{j+1},{k},{random_temperature}")


        with open("weather_logs.csv", "w") as f:
            f.write("Season,Day,Hour,Temperature\n")
            for line in csv_array:
                f.write(f"{line}\n")

        messagebox.showinfo(
            "Success",
            "Weather data has been logged successfully."
        )

        self.win.destroy()


def main():
    logger = WeatherLogger()
    logger.run()


if __name__ == "__main__":
    main()
