from tkinter import Tk, Frame, Entry, Button, Label, Toplevel, StringVar, OptionMenu
from backend import Laptop, GamingLaptop, ShoppingCart

class LaptopShopApp:
    ram_options = {4, 8, 16, 32}
    gpu_options = {"NVIDIA GTX 1650", "NVIDIA RTX 3070", "NVIDIA RTX 4080", "AMD RX 6800M"}

    def __init__(self, shopping_cart=None):
        self.win = Tk()
        self.win.title("Laptop Shop")
        self.shopping_cart = shopping_cart or ShoppingCart()

        self.main_frame = Frame(self.win)
        self.main_frame.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
        )

        self.ram_var = StringVar()
        self.laptop_type_var = StringVar()

        self.widgets = []

    def run(self):
        self.create_widgets()
        self.win.mainloop()

    def create_widgets(self):
        self.delete_all_widgets()

        for i, laptop in enumerate(self.shopping_cart.laptops):
            label = Label(
                self.main_frame,
                text=f"{laptop.brand} (Ram: {laptop.ram}GB) (Price: £{laptop.calculate_price()})"
            )
            label.grid(row=i, column=0)
            self.widgets.append(label)

            modify_button = Button(
                self.main_frame,
                text="Modify",
                command=lambda i=i: self.modify_laptop(i)
            )
            modify_button.grid(row=i, column=1)
            self.widgets.append(modify_button)

            delete_button = Button(
                self.main_frame,
                text="Delete",
                command=lambda i=i: self.delete_laptop(i)
            )
            delete_button.grid(row=i, column=2)
            self.widgets.append(delete_button)

        total_price_label = Label(
            self.main_frame,
            text="Total price: £" + str(self.shopping_cart.total)
        )
        total_price_label.grid(row=len(self.shopping_cart.laptops), column=0)
        self.widgets.append(total_price_label)

        add_laptop_button = Button(
            self.main_frame,
            text="Add Laptop",
            command=self.add_laptop
        )
        add_laptop_button.grid(row=len(self.shopping_cart.laptops) + 1, column=0)
        self.widgets.append(add_laptop_button)

    def delete_all_widgets(self):
        for widget in self.widgets:
            widget.destroy()
        self.widgets = []

    def modify_laptop(self, index):
        laptop = self.shopping_cart.laptops[index]
        modify_laptop_win = Toplevel(self.win)
        modify_laptop_win.title("Modify Laptop")

        brand_label = Label(
            modify_laptop_win,
            text="Brand:"
        )
        brand_label.grid(row=0, column=0)

        brand_entry = Entry(modify_laptop_win)
        brand_entry.insert(0, laptop.brand)
        brand_entry.grid(row=0, column=1)

        ram_label = Label(
            modify_laptop_win,
            text="Ram:"
        )
        ram_label.grid(row=1, column=0)

        ram_options = OptionMenu(
            modify_laptop_win,
            self.ram_var,
            *self.ram_options,
            command=lambda value: self.ram_var.set(value)
        )
        ram_options.grid(row=1, column=1)
        self.ram_var.set(laptop.ram)

        base_price_label = Label(
            modify_laptop_win,
            text="Base Price:"
        )
        base_price_label.grid(row=2, column=0)

        base_price_entry = Entry(modify_laptop_win)
        base_price_entry.insert(0, laptop.base_price)
        base_price_entry.grid(row=2, column=1)

        laptop_type_label = Label(
            modify_laptop_win,
            text="Laptop Type:"
        )
        laptop_type_label.grid(row=3, column=0)

        laptop_type_options = OptionMenu(
            modify_laptop_win,
            self.laptop_type_var,
            "Standard",
            "Gaming",
            command=lambda value: self.laptop_type_var.set(value)
        )
        laptop_type_options.grid(row=3, column=1)
        self.laptop_type_var.set("Gaming")

        if isinstance(laptop, GamingLaptop):
            gpu_label = Label(
                modify_laptop_win,
                text="GPU:"
            )
            gpu_label.grid(row=4, column=0)

            gpu_options = OptionMenu(
                modify_laptop_win,
                self.laptop_type_var,
                *self.gpu_options,
                command=lambda value: self.laptop_gpu.set(value)
            )
            gpu_options.grid(row=4, column=1)
            self.laptop_type_var.set(laptop.gpu)


        save_laptop_button = Button(
            modify_laptop_win,
            text="Save",
            command=lambda: self.save_laptop(
                modify_laptop_win,
                index,
                brand_entry.get(),
                self.ram_var.get(),
                base_price_entry.get(),
                self.laptop_type_var.get()
            )
        )
        save_laptop_button.grid(row=4, column=0)

    def save_laptop(self, window, index, brand, ram, base_price, laptop_type):
        if laptop_type == "Standard":
            laptop = Laptop(brand, int(base_price))
        else:
            laptop = GamingLaptop(brand, int(base_price))
            laptop.gpu = "NVIDIA GTX 1650"
        laptop.ram = int(ram)
        self.shopping_cart.laptops[index] = laptop
        self.create_widgets()
        window.destroy()

    def delete_laptop(self, index):
        self.shopping_cart.laptops.pop(index)
        self.create_widgets()

    def add_laptop(self):
        add_laptop_win = Toplevel(self.win)
        add_laptop_win.title("Add Laptop")

        brand_label = Label(
            add_laptop_win,
            text="Brand:"
        )
        brand_label.grid(row=0, column=0)

        brand_entry = Entry(add_laptop_win)
        brand_entry.grid(row=0, column=1)

        ram_label = Label(
            add_laptop_win,
            text="Ram:"
        )
        ram_label.grid(row=1, column=0)

        ram_options = OptionMenu(
            add_laptop_win,
            self.ram_var,
            *self.ram_options,
            command=lambda value: self.ram_var.set(value)
        )
        ram_options.grid(row=1, column=1)
        self.ram_var.set(4)

        base_price_label = Label(
            add_laptop_win,
            text="Base Price:"
        )
        base_price_label.grid(row=2, column=0)

        base_price_entry = Entry(add_laptop_win)
        base_price_entry.grid(row=2, column=1)

        laptop_type_label = Label(
            add_laptop_win,
            text="Laptop Type:"
        )
        laptop_type_label.grid(row=3, column=0)

        laptop_type_options = OptionMenu(
            add_laptop_win,
            self.laptop_type_var,
            "Standard",
            "Gaming",
            command=lambda value: self.laptop_type_var.set(value)
        )
        laptop_type_options.grid(row=3, column=1)
        self.laptop_type_var.set("Gaming")

        add_laptop_button = Button(
            add_laptop_win,
            text="Add",
            command=lambda: self.add_laptop_to_cart(
                add_laptop_win,
                brand_entry.get(),
                self.ram_var.get(),
                base_price_entry.get(),
                self.laptop_type_var.get()
            )
        )
        add_laptop_button.grid(row=4, column=0)

    def add_laptop_to_cart(self, window, brand, ram, base_price, laptop_type):
        if laptop_type == "Standard":
            laptop = Laptop(brand, int(base_price))
        else:
            laptop = GamingLaptop(brand, int(base_price))
            laptop.gpu = "NVIDIA GTX 1650"
        laptop.ram = int(ram)
        self.shopping_cart.add_laptop(laptop)
        self.create_widgets()
        window.destroy()



def main():
    app = LaptopShopApp()
    app.shopping_cart.add_laptop(Laptop("Dell", 500))
    app.shopping_cart.laptops[0].ram = 8
    app.shopping_cart.add_laptop(Laptop("Apple", 1000))
    app.shopping_cart.add_laptop(GamingLaptop("Razer", 2000))
    app.run()

if __name__ == "__main__":
    main()
