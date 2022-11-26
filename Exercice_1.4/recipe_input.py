# “recipe_input.py” takes recipes from the user, compiles them and their ingredients into a list, and stores all this in a binary file for later use. The script can be run again later to add more recipes.

# Imports pickle to work with binary files
import pickle

# Initializes two empty lists
recipes_list = []
ingredients_list = []

# Defines take_recipe function
def take_recipe():
  recipe_ingredients = []

  # Asks the user to input recipe name
  name = str(input("\nEnter the name of the recipe: "))

  # Asks the user to input cooking time
  cooking_time = int(input("Enter the cooking time (minutes): "))
  
  # Asks the user to input ingredients
  add_ingredient = True

  # Asks the user to input ingredients until he types "n" when asked if he wants to enter more ingredients
  while (add_ingredient == True):
    ingredient = input("Enter an ingredient: ")
    recipe_ingredients.append(ingredient)

    add_ingredient_req = input("Do you want to add a new ingredient? (y/n): ")
    if add_ingredient_req == "y":
      add_ingredient = True
    elif add_ingredient_req == "n":
      add_ingredient = False
    else:
      print("Wrong entry, please try again.")
      add_ingredient_req = input("Do you want to add a new ingredient? (y/n): ")

  # Calls the calc_difficulty() function to define the recipe level of difficulty and assign the returned difficulty to difficulty variable
  difficulty = calc_difficulty(cooking_time, recipe_ingredients)

  # Creates a dictionary that stores recipe details
  recipe = {
    "name": name,
    "cooking_time": cooking_time,
    "recipe_ingredients": recipe_ingredients,
    "difficulty": difficulty,
  }

  return recipe


def calc_difficulty(cooking_time, recipe_ingredients):
  print("Run the calc_difficulty with: ", cooking_time, recipe_ingredients)

  if (cooking_time < 10) and (len(recipe_ingredients) < 4):
    difficulty_level = "Easy"
  elif (cooking_time < 10) and (len(recipe_ingredients) >= 4):
    difficulty_level = "Medium"
  elif (cooking_time >= 10) and (len(recipe_ingredients) < 4):
    difficulty_level = "Intermediate"
  elif (cooking_time >= 10) and (len(recipe_ingredients) >= 4):
     difficulty_level = "Hard"
  else:
    print("Something bad happened, please try again")
  
  print("Difficulty level: ", difficulty_level)
  return difficulty_level


# =========
# MAIN CODE
# =========

try:
  recipe_file_name = input("Enter the name of the file that contains your recipe data (including the .bin extension): ")
  # Attempts to open a binary file in read mode
  my_recipes_file = open(recipe_file_name, 'rb')

  # Loads the dictionary into data variable
  data = pickle.load(my_recipes_file)

except FileNotFoundError:
  print("File doesn't exist - exiting.")

  # Create a new dictionary
  data = {
    "recipes_list": [],
    "all_ingredients": [],
  }

except:
  print("An unexpected error occurred.")

  # Create a new dictionary
  data = {
    "recipes_list": [],
    "all_ingredients": [],
  }

else:
  # Close the binary file
  my_recipes_file.close()

finally:
  # data = pickle.load(my_recipes_file)
  recipes_list = data["recipes_list"]
  ingredients_list = data["all_ingredients"]
  print("Data from finally: ", data)
  print("Recipes list from finally: ", recipes_list)
  print("Ingredient list from finally: ", ingredients_list)


  # Asks the user how many recipes he would like to enter
  n = int(input("Please specify how many recipes you want to enter: "))

  # Loops n times through the take_recipe() function to collect the n recipes details
  for n in range(0,n):
    # Calls the take_recipe() function and store the returned dictionary into recipe variable
    recipe = take_recipe()
    print("Recipe dictionary: ", recipe)

    # Appends the new recipe to the recipes_list global variable
    recipes_list.append(recipe)

    # -- PRINT OUT THE RECIPE NAME: --
    print("\nRecipe: ", recipe["name"])

    # -- PRINTS OUT THE RECIPE COOKING TIME: --
    print("Cooking Time (min): ", recipe["cooking_time"])

    # -- PRINTS OUT THE RECIPE INGREDIENTS: --
    # Loops through recipe’s ingredients list, where it picks out elements one-by-one as ingredient
    # print("Recipe ingredients list: ", recipe["recipe_ingredients"])
    print("Ingredients: ")
    for ele in recipe["recipe_ingredients"]:
      print(ele)
      if ele in ingredients_list:
        continue
      else:
        ingredients_list.append(ele)

    # -- PRINTS OUT THE RECIPE DIFFICULTY LEVEL: --
    calc_difficulty(recipe["cooking_time"], recipe["recipe_ingredients"])

  # -- PRINTS OUT ALL THE INGREDIENTS ACCROSS ALL RECIPES (SORTED IN ALPHABETICAL ORDER): --
  # print(ingredients_list)
  ingredients_list.sort()
  # print(ingredients_list)

  print("\n\nIngredients Available Accross All Recipies: ")
  print("--------------------------------------------")
  for ingredient in ingredients_list:
    print(ingredient)

  # Gathers recipes_list and all_ingredients into a dictionary called data
  data = {
    "recipes_list": recipes_list,
    "all_ingredients": ingredients_list,
  }

  print("Data from the data variable: ", data)

  # Opens a binary file
  my_recipes_file = open(recipe_file_name, 'wb')

  # Write data dictionary into the binary file
  pickle.dump(data, my_recipes_file)

  # Close the binary file
  my_recipes_file.close()

