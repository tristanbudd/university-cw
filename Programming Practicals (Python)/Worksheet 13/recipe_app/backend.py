class Recipe:
    def __init__(self, name, cook_time, instructions):
        self.name = name
        self.cook_time = cook_time
        self.instructions = instructions


class RecipeBook:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def remove_recipe(self, recipe_name):
        for recipe in self.recipes:
            if recipe.name == recipe_name:
                self.recipes.remove(recipe)
                return True
        return False

    def get_recipes(self):
        return self.recipes

    def get_recipe_by_index(self, index):
        if index < len(self.recipes):
            return self.recipes[index]
        return None