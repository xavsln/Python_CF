class Recipe(object):

  all_ingredients = []

  def __init__(self, name):
    self.name = name
    self.ingredients = []
    self.cooking_time = int(0)
    self.difficulty = ""

  def get_name(self):
    output = "Recipe name: " + str(self.name)
    return output

  def set_name(self, name):
    self.name = str(name)

  def get_cooking_time(self):
    output = "Cooking time: " + str(self.cooking_time)
    return output

  def set_cooking_time(self, cooking_time):
    self.cooking_time = int(cooking_time)

  # Takes in variable-length arguments for the recipe’s ingredients
  def add_ingredients(self, *args):
    # print(args)
    self.ingredients = args
    # print(self.ingredients)
    # Add ingredients in case they are not already in the all recipes ingredients list
    self.update_all_ingredients()

  # Returns the recipe ingredients list
  def get_ingredients(self):
    print("\nIngredients: ")
    print("---------------------------")
    for ingredient in self.ingredients:
      print(' - ' + str(ingredient))
    print("\n")

  def get_difficulty(self):
    difficulty = self.calc_difficulty(self.cooking_time, self.ingredients)
    output = "Difficulty: " + str(self.cooking_time)
    self.difficulty = difficulty
    # print("Difficulty: ", difficulty)
    return output

  def calc_difficulty(self, cooking_time, ingredients):
    # print("Run the calc_difficulty with: ", cooking_time, ingredients)

    if (cooking_time < 10) and (len(ingredients) < 4):
      difficulty_level = "Easy"
    elif (cooking_time < 10) and (len(ingredients) >= 4):
      difficulty_level = "Medium"
    elif (cooking_time >= 10) and (len(ingredients) < 4):
      difficulty_level = "Intermediate"
    elif (cooking_time >= 10) and (len(ingredients) >= 4):
      difficulty_level = "Hard"
    else:
      print("Something bad happened, please try again")
    
    # print("Difficulty level: ", difficulty_level)
    return difficulty_level

  # Checks the ingredients of the recipe and in case an ingredient is not already in the all_ingredients list, append the ingredient to the list in order to keep track of all the ingredients that exist across all recipes.
  def update_all_ingredients(self):
    for ingredient in self.ingredients:
      # print("Ingredients from update_all_ingredients: ", ingredient)
      if ingredient not in self.all_ingredients:
        # print("Ingredient added to the list")
        self.all_ingredients.append(ingredient)

  # Takes an ingredient as an argument, searches for it in the recipe, and returns True or False appropriately
  def search_ingredient(self, ingredient, ingredients):
    if (ingredient in ingredients):
      # print("Ingredient in the ingredients list.")
      return True
    else:
      # print("Ingredient not in the ingredients list.")
      return False

  # Finds recipes that contain a specific ingredient
  def recipe_search(self, recipes_list, ingredient):
    data = recipes_list
    search_term = ingredient
    for recipe in data:
      # print("Recipe.name: ", recipe.name)
      # print("Recipe.ingredients: ", recipe.ingredients)
      if self.search_ingredient(search_term, recipe.ingredients):
        print(recipe)

    # print("search_term: ", search_term)

  def __str__(self):
    output = "\nName: " + str(self.name) + \
        "\nCooking time (minutes): " + str(self.cooking_time) + \
        "\nDifficulty: " + str(self.difficulty) + \
        "\nIngredients:" + \
        "\n------------ \n"
    for ingredient in self.ingredients:
        output += "- " + ingredient + "\n"
    return output

  def view_recipe(self):
    print("\nName: " + str(self.name))
    print("Cooking time: " + str(self.cooking_time))
    self.get_ingredients()

recipes_list = []

# Makes a tea object
tea = Recipe("Tea")
tea.add_ingredients("Tea Leaves", "Sugar", "Water")
tea.set_cooking_time(5)
tea.get_difficulty()
# print(tea)
# print(tea.all_ingredients)

recipes_list.append(tea)

# Makes a coffee object and add it to the recipes_list
coffee = Recipe("Coffee")
coffee.add_ingredients("Coffee Powder", "Sugar", "Water")
coffee.set_cooking_time(5)
coffee.get_difficulty()
# print(coffee)
# print(coffee.all_ingredients)

recipes_list.append(coffee)

# Makes a cake object and add it to the recipes_list
cake = Recipe("Cake")
cake.add_ingredients("Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk")
cake.set_cooking_time(50)
cake.get_difficulty()
# print(cake)

# cake.update_all_ingredients()
# print(cake.all_ingredients)

recipes_list.append(cake)

# Makes a banana_smoothie object and add it to the recipes_list
banana_smoothie = Recipe("Banana Smoothie")
banana_smoothie.add_ingredients("Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes")
banana_smoothie.set_cooking_time(5)
banana_smoothie.get_difficulty()
# print(banana_smoothie)
# print(banana_smoothie.all_ingredients)

recipes_list.append(banana_smoothie)

# Prints the recipes_list
print("------------- ")
print("Recipes list: ")
print("------------- ")
for recipe in recipes_list:
  print(recipe)

# Search for recipes that contain some ingredient (Water, Sugar, Bananas)
print("------------------------------------- ")
print("Results for recipe_search with Water: ")
print("------------------------------------- ")
tea.recipe_search(recipes_list, "Water")

print("------------------------------------- ")
print("Results for recipe_search with Sugar: ")
print("------------------------------------- ")
tea.recipe_search(recipes_list, "Sugar")

print("--------------------------------------- ")
print("Results for recipe_search with Bananas: ")
print("--------------------------------------- ")
tea.recipe_search(recipes_list, "Bananas")