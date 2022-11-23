# Initializes two empty lists
recipes_list = []
ingredients_list = []

# Defines take_recipe function
def take_recipe():
  recipe_ingredients = []

  # Asks the user to input recipe name
  name = str(input("\nEnter the name of the recipe: "))

  # Asks the user to input cooking time
  cooking_time = int(input("Enter the cooking time: "))
  
  # Asks the user to input ingredients
  add_ingredient = True

  # Asks the user to input ingredients until he types "n" when asked if he wants to enter more ingredients
  while (add_ingredient == True):
    ingredient = input("Enter an ingredient: ")
    recipe_ingredients.append(ingredient)

    add_ingredient_req = input("Do you want to add a new ingredient?: ")
    if add_ingredient_req == "y":
      add_ingredient = True
    elif add_ingredient_req == "n":
      add_ingredient = False
    else:
      print("Wrong entry, please try again.")
      add_ingredient_req = input("Do you want to add a new ingredient?: ")

  # Create a dictionary that stores recipe details
  recipe = {
    "name": name,
    "cooking_time": cooking_time,
    "recipe_ingredients": recipe_ingredients,
  }

  return recipe


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
  # Determine the difficulty of the recipe
  if (recipe["cooking_time"] < 10) and (len(recipe["recipe_ingredients"]) < 4):
    difficulty = "Easy"
  elif (recipe["cooking_time"] < 10) and (len(recipe["recipe_ingredients"]) >= 4):
    difficulty = "Medium"
  elif (recipe["cooking_time"] >= 10) and (len(recipe["recipe_ingredients"]) < 4):
    difficulty = "Intermediate"
  elif (recipe["cooking_time"] >= 10) and (len(recipe["recipe_ingredients"]) >= 4):
     difficulty = "Hard"
  else:
    print("Something bad happened, please try again")
  
  print("Difficulty level: ", difficulty)

# -- PRINTS OUT ALL THE INGREDIENTS ACCROSS ALL RECIPES (SORTED IN ALPHABETICAL ORDER): --
# print(ingredients_list)
ingredients_list.sort()
# print(ingredients_list)

print("\n\nIngredients Available Accross All Recipies: ")
print("--------------------------------------------")
for ingredient in ingredients_list:
  print(ingredient)


