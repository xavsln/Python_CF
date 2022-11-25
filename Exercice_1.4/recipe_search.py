import pickle

# =========================
# display_recipe() function
# =========================
# Takes in one recipe (of the dictionary type) as an argument and prints all of its attributes including the recipe name, cooking time, ingredients, and difficulty.
def display_recipe(recipe):
  # print(recipe)

  # -- PRINT OUT THE RECIPE NAME: --
  print("\nRecipe: ", recipe["name"])

  # -- PRINTS OUT THE RECIPE COOKING TIME: --
  print("Cooking Time (minutes): ", recipe["cooking_time"])

  # -- PRINTS OUT THE RECIPE INGREDIENTS: --
  # Loops through recipe’s ingredients list, where it picks out elements one-by-one as ingredient
  # print("Recipe ingredients list: ", recipe["recipe_ingredients"])
  print("Ingredients: ")
  for ele in recipe["recipe_ingredients"]:
    print(ele)
    # if ele in ingredients_list:
    #   continue
    # else:
    #   ingredients_list.append(ele)

  # -- PRINTS OUT THE RECIPE DIFFICULTY LEVEL: --
  print("Difficulty level: ", recipe["difficulty"])


# ============================
# search_ingredient() function
# ============================
# Searches for an ingredient in the given data. The function takes in a dictionary called data as its argument.
def search_ingredient(data):
  # Shows the user all the available ingredients contained in data
  # print("All ingredients can be found here: ", data["all_ingredients"])
  all_ingredients_list = list(enumerate(data["all_ingredients"]))
  # print(all_ingredients_list)
  
  for index, tup in enumerate(all_ingredients_list):
    print(str(tup[0]+1) + ". " + tup[1])

  try:
    # User to pick a number from the all_ingredients_list. This number is used as the index to retrieve the corresponding ingredient, which is then stored into a variable called ingredient_searched
    ingredient_searched_nber = input("Enter the number corresponding to the ingredient you want to select from the above list: ")

    ingredient_searched_index = int(ingredient_searched_nber) - 1

    ingredient_searched = all_ingredients_list[ingredient_searched_index][1]

    print("\nYou selected the ingredient: ", ingredient_searched)

  except:
    print("An unexpected error occurred. Make sure to select a number from the list.")

  else:
    # Iterates through the list of recipes in the data dictionary
    for recipe in data["recipes_list"]:
      # print(recipe)
      for recipe_ing in recipe["recipe_ingredients"]:
        # print(recipe_ing)
        if (recipe_ing == ingredient_searched):
          print("\nThe following recipe includes the searched ingredient:")
          print("------------------------------------------------------")
          display_recipe(recipe)

# =========
# MAIN CODE
# =========

recipe_file_name = input("Enter the name of the file that contains your recipe data (including the .bin extension): ")

try: 
  user_recipe_file = open(recipe_file_name, "rb")
  data = pickle.load(user_recipe_file)
  # print(data)

except FileNotFoundError:
  print("File doesn't exist - exiting.")

# Else block is a variation of the finally block. However it is executed only if the try block doesn't encounter any error
# Calls search_ingredient() while passing data into it as an argument.
else:
  search_ingredient(data)
  user_recipe_file.close()
