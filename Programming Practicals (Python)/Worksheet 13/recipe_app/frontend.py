from tkinter import Tk, Frame, Entry, Button, Label, StringVar, Toplevel, Text
from backend import Recipe, RecipeBook

class RecipeApp:

    def __init__(self, recipe_book):
        self.recipe_book = recipe_book

        self.win = Tk()
        self.win.title("Recipe Book")

        self.main_frame = Frame(self.win)
        self.main_frame.grid(row=0, column=0, padx=10, pady=10)

        self.recipe_widgets = []

    def run(self):
        self.create_widgets()
        self.win.mainloop()

    def create_widgets(self):
        self.delete_all_recipe_widgets()

        recipes = self.recipe_book.get_recipes()
        for i, recipe in enumerate(recipes):
            recipe_frame = Frame(self.main_frame)
            recipe_frame.grid(row=i, column=0, padx=10, pady=10)

            recipe_name_label = Label(
                recipe_frame,
                text=recipe.name
            )
            recipe_name_label.grid(row=0, column=0)

            recipe_cook_time_label = Label(
                recipe_frame,
                text=f"{recipe.cook_time} mins"
            )
            recipe_cook_time_label.grid(row=0, column=1)

            recipe_view_button = Button(
                recipe_frame,
                text="View Recipe",
                command=lambda r=recipe: self.view_recipe(r)
            )
            recipe_view_button.grid(row=0, column=2)

            self.recipe_widgets.append(recipe_frame)

    def delete_all_recipe_widgets(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def view_recipe(self, recipe):
        view_recipe_win = Toplevel(self.win)
        view_recipe_win.title(recipe.name)

        recipe_name = Label(
            view_recipe_win,
            font=("Arial", 16),
            text=recipe.name
        )
        recipe_name.grid(row=0, column=0)

        recipe_cook_time = Label(
            view_recipe_win,
            text=f"Cook time: {recipe.cook_time} minutes"
        )
        recipe_cook_time.grid(row=1, column=0)

        recipe_instructions = Text(view_recipe_win)
        for i, instruction in enumerate(recipe.instructions):
            recipe_instructions.insert(f"{i + 1}.0", f"Step {i+1}: {instruction}\n")
        recipe_instructions.grid(row=2, column=0, padx=10, pady=10)

def main():
    recipe_book = RecipeBook()
    recipe1 = Recipe("Pasta", 30, ["Boil pasta", "add sauce", "mix well"])
    recipe2 = Recipe("Salad", 15, ["Chop vegetables", "add dressing", "toss well"])
    recipe_book.add_recipe(recipe1)
    recipe_book.add_recipe(recipe2)

    app = RecipeApp(recipe_book)
    app.run()

if __name__ == "__main__":
    main()