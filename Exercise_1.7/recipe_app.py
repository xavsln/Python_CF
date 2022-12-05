# Creates an engine object called engine that connects to your desired database.
from sqlalchemy import create_engine
engine = create_engine("mysql://cf-python:password@localhost/my_database")

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column
from sqlalchemy.types import Integer, String

# Declares Recipe Class that inherits from Base
class Recipe(Base):
  __tablename__ = "final_recipes"

  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(50))
  ingredients = Column(String(255))
  cooking_time = Column(Integer)
  difficulty = Column(String(20))

  def __repr__(self):
    return "<Recipe ID: " + str(self.id) + "-" + self.name + ">"

  def __str__(self):
    output = "\nName: " + str(self.name) + \
      "\nCooking time (minutes): " + str(self.cooking_time) + \
      "\nDifficulty: " + str(self.difficulty) + \
      "\nIngredients: " + str(self.ingredients)
    return output

# Create tables of all models defined
Base.metadata.create_all(engine)

# Creates a session object that will be used to make changes to the database
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

# calculate_difficulty() calculates the difficulty of the recipe by taking in cooking_time and ingredients as arguments, and assign the difficulty level as a strings: Easy, Medium, Intermediate, or Hard to the difficulty variable
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

  # return_ingredients_as_list() function retrieves the ingredients string inside Recipe object as a list
def return_ingredients_as_list():
  # assign all recipes to recipes_list
  recipes_list = session.query(Recipe).all()
  for recipe in recipes_list:
    print("Recipe: ", recipe)
    print("recipe.ingredients: ", recipe.ingredients)
    # split the strings and create a list and 
    recipe_ingredients_list = recipe.ingredients.split(", ")
    print(recipe_ingredients_list)


# ====================================
# Main Menu - create_recipe() function
# ====================================
# Function below allows the user to input a new recipe data (name, cooking time, ingredients) and also automatically determines a difficulty level based on cooking time and number of ingredients
def create_recipe():
  recipe_ingredients = []

  # Keep prompting the user until they enter a name < 50 with only alphabetical characters and numeric cooking time
  correct_input_name = False
  while correct_input_name == False:
    
    # Asks the user to input recipe name
    name = input("\nEnter the name of the recipe: ")
    if len(name) < 50:

      correct_input_name = True

      correct_input_cooking_time = False
      while correct_input_cooking_time == False:
        # Asks the user to input cooking time
        cooking_time = input("\nEnter the cooking time of the recipe (minutes): ")
        if cooking_time.isnumeric() == True:
          correct_input_cooking_time = True
      
        else:
          # correct_input_cooking_time = False
          print("Please enter a number.")
    
    else:
      # correct_input_name = False
      print("Please enter a name that contains less than 50 characters.")

    # --- ENTERS INGREDIENTS --- #
    # Asks the user to enter the number of ingredients he wants to add
    # Then, asks the user to input ingredients
    correct_input_number = False
    while correct_input_number == False:
      ing_nber = input("How many ingredients do you want to enter?: ")
      if ing_nber.isnumeric() == True:
        correct_input_number = True

        for _ in range(int(ing_nber)):
          ingredient = input("Enter an ingredient: ")
          recipe_ingredients.append(ingredient)

      else:
        correct_input_number = False
        print("Please enter a positive number.")

  # --- CONVERT INGREDIENTS LIST INTO A STRING --- #

  # Converts recipe_ingredients into comma-separated strings as MySQL doesn't fully support arrays
  recipe_ingredients_str = ", ".join(recipe_ingredients)
  print(recipe_ingredients_str)

  # --- GENERATE DIFFICULTY ATTRIBUTE FOR THE RECIPE --- #
  
  # Call calculate_difficulty() that calculates the difficulty of the recipe by taking in cooking_time and ingredients as arguments, and returning one of the following strings: Easy, Medium, Intermediate, or Hard
  difficulty = calc_difficulty(int(cooking_time), recipe_ingredients)

  # --- CREATE A NEW OBJECT FROM RECIPE MODEL CALLED recipe_entry --- #

  recipe_entry = Recipe(
    name = name,
    cooking_time = int(cooking_time),
    ingredients = recipe_ingredients_str,
    difficulty = difficulty
  )

  print(recipe_entry)

  # --- ADD THE RECIPE TO THE final_recipes TABLE AND COMMIT THE CHANGES --- #

  session.add(recipe_entry)
  session.commit()

  print("Recipe saved into the database.")


# =======================================
# Main Menu - view_all_recipes() function
# =======================================

def view_all_recipes():
  all_recipes = []
  all_recipes = session.query(Recipe).all()

  # print("len(all_recipes): ", len(all_recipes))

  # If there aren’t any entries, inform the user that there aren’t any entries in your database
  if len(all_recipes) == 0:
    print("There is no recipe in the database")
    return None

  # Else, print all the recipes entered in the database
  else:
    print("\nAll recipes can be found below: ")
    print("-------------------------------------------")

    for recipe in all_recipes:
      print(recipe)


# ============================================
# Main Menu - search_by_ingredients() function
# ============================================
def search_by_ingredients():
  # Check if your table has any entries. If there aren’t any entries, notify the user, and exit the function.
  if session.query(Recipe).count() == 0:
    print("There is no recipe in the database")
    return None

  else:
    # Retrieve only the values from the ingredients column of the table, and store them into a variable called results.
    results = session.query(Recipe.ingredients).all()
    print("results: ", results)

    # Initialize an empty list called all_ingredients
    all_ingredients = []

    # Iterates through the results list and for each recipe ingredients tuple
    for recipe_ingredients_list in results:
      # Iterate through recipe ingredients tuple
      for recipe_ingredients in recipe_ingredients_list:
        # split each recipe ingredients tuple
        recipe_ingredient_split = recipe_ingredients.split(", ")
        all_ingredients.extend(recipe_ingredient_split)

    print("all_ingredients after the loop: ", all_ingredients)

    # Remove all duplicates from the list
    all_ingredients = list(dict.fromkeys(all_ingredients))

    # Shows the user all the available ingredients contained in all_ingredients
    all_ingredients_list = list(enumerate(all_ingredients))

    print("\nAll ingredients list:")
    print("------------------------")

    for index, tup in enumerate(all_ingredients_list):
      print(str(tup[0]+1) + ". " + tup[1])

    try:
      # User to pick a number from the all_ingredients_list. This number is used as the index to retrieve the corresponding ingredient, which is then stored into a variable called ingredient_searched
      ingredient_searched_nber = input("\nEnter the number corresponding to the ingredient you want to select from the above list. You can enter several numbers. In this case, numbers shall be separated by a space: ")

      # create a list to identify the different ingredients user wants to search
      ingredients_nber_list_searched = ingredient_searched_nber.split(" ")

      # iterate through the list of ingredients nber searched and associate a ingredient name

      ingredient_searched_list = []
      for ingredient_searched_nber in ingredients_nber_list_searched:
        ingredient_searched_index = int(ingredient_searched_nber) - 1
        ingredient_searched = all_ingredients_list[ingredient_searched_index][1]

        ingredient_searched_list.append(ingredient_searched)

      print("\nYou selected the ingredient(s): ", ingredient_searched_list)

      # Initialize an empty list called conditions. This list will contain like() conditions for every ingredient to be searched for

      conditions = []

      # Run a loop that runs through ingredient_searched_list
      for ingredient in ingredient_searched_list:
        like_term = "%"+ingredient+"%"
        # print("like_term: ", '"' +like_term+ '"')
        # Append the search condition containing like_term to the conditions list
        condition = Recipe.ingredients.like(like_term)
        conditions.append(condition)
      print("conditions: ", conditions)

      # Retrieve all recipes from the database using the filter() query, containing the list conditions
      # conditions_test = [Recipe.ingredients.like("%Water%"), Recipe.ingredients.like("%Sugar%")]
      # print(conditions_test)
      searched_recipes = session.query(Recipe).filter(*conditions).all()
      
      print(searched_recipes)

    except:
      print("An unexpected error occurred. Make sure to select a number from the list.")

    else:

      print("searched_recipes: ")
      for recipe in searched_recipes:
        print(recipe)


# ====================================
# Main Menu - delete_recipe() function
# ====================================
def delete_recipe():
  # Check if your table has any entries. If there aren’t any entries, notify the user, and exit the function.
  if session.query(Recipe).count() == 0:
    print("There is no recipe in the database")
    return None

  else:
    # Retrieve only the values from the id and name columns of the table, and store them into a variable called results.
    results = session.query(Recipe).with_entities(Recipe.id, Recipe.name).all()
    print("results: ", results)
    print("Lits of available recipes:")
    for recipe in results:
      print("\nId: ", recipe[0])
      print("Name: ", recipe[1])
    # Initialize an empty list called all_ingredients
    # all_ingredients = []

    # Asks the user to input the ID of the recipe he wants to delete
    recipe_id_for_deletion = (input("\nEnter the ID of the recipe you want to delete: "))

    # Look for the object associated with the ID and retrieve it
    recipe_to_be_deleted = session.query(Recipe).filter(Recipe.id == recipe_id_for_deletion).one()

    print("\nWARNING: You are about to delete the following recipe: ")
    print(recipe_to_be_deleted)

    # Confirm with the user he wants to delete this entry
    deletion_confirmed = input("\nPlease confirm you want to delete the entry above (y/n): ")
    if deletion_confirmed == "y":
      # Delete the corresponding recipe into result  
      session.delete(recipe_to_be_deleted)

      # Commits changes made to the final_recipes table
      session.commit()
      print("\nRecipe successfully deleted from the database.")
    else:
      return None
      

# ====================================
# Main Menu - edit_recipe() function
# ====================================
def edit_recipe():
  # Check if your table has any entries. If there aren’t any entries, notify the user, and exit the function.
  if session.query(Recipe).count() == 0:
    print("There is no recipe in the database")
    return None

  else:
    # Retrieve only the values from the id and name columns of the table, and store them into a variable called results.
    results = session.query(Recipe).with_entities(Recipe.id, Recipe.name).all()
    print("results: ", results)
    print("Lits of available recipes:")
    for recipe in results:
      print("\nId: ", recipe[0])
      print("Name: ", recipe[1])
    # Initialize an empty list called all_ingredients
    # all_ingredients = []

    # Asks the user to input the ID of the recipe he wants to edit
    recipe_id_for_edit = int((input("\nEnter the ID of the recipe you want to delete: ")))

    print(session.query(Recipe).with_entities(Recipe.id).all())

    recipes_id_tup_list = session.query(Recipe).with_entities(Recipe.id).all()
    recipes_id_list = []

    for recipe_tup in recipes_id_tup_list:
      print(recipe_tup[0])
      recipes_id_list.append(recipe_tup[0])

    print(recipes_id_list)

    if recipe_id_for_edit not in recipes_id_list:
      print("Not in the ID list, please try again later.")
    else:
      print("Ok you can continue")
      # Look for the object associated with the ID and retrieve it
      recipe_to_edit = session.query(Recipe).filter(Recipe.id == recipe_id_for_edit).one()
      
      print("\nWARNING: You are about to edit the following recipe: ")
      print(recipe_to_edit)

      # Asks the user to input which column he wants to update among name, cooking_time and ingredients
      column_for_update = int(input("\nEnter the data you want to update among 1. name, 2. cooking time and 3. ingredients: (select '1' or '2' or '3'): "))

      # Asks the user to input the new value
      updated_value = (input("\nEnter the new value for the recipe: "))
      print("Choice: ", updated_value)

      if column_for_update == 1: 
        print("You want to update the name of the recipe")
        session.query(Recipe).filter(Recipe.id == recipe_id_for_edit).update({Recipe.name: updated_value})
        session.commit()

      elif column_for_update == 2: 
        print("You want to update the cooking time of the recipe")
        session.query(Recipe).filter(Recipe.id == recipe_id_for_edit).update({Recipe.cooking_time: updated_value})
        session.commit()

      elif column_for_update == 3: 
        print("You want to update the ingredients of the recipe")
        session.query(Recipe).filter(Recipe.id == recipe_id_for_edit).update({Recipe.ingredients: updated_value})
        session.commit()

      else:
        print("Wrong input, please try again.")

      # Recalculate the difficulty
      updated_difficulty = calc_difficulty(recipe_to_edit.cooking_time, recipe_to_edit.ingredients)
      print("updated_difficulty: ", updated_difficulty)

      # Assign the updated difficulty to edited recipe
      recipe_to_edit.difficulty = updated_difficulty

      # Commit changes to the database
      session.commit()
      print("Modification done.")


# ====================================
# Main Menu - main_menu() function
# ====================================

def main_menu():
  # Loops until the user decides to type "quit"
  choice = ""
  while(choice != "quit"):
    print("\n======================================================")
    print("\nMain Menu:")
    print("-------------")
    print("Pick a choice:")
    print("   1. Create a new recipe")
    print("   2. Search for a recipe by ingredient")
    print("   3. Edit an existing recipe")
    print("   4. Delete a recipe")
    print("   5. View all recipes")
    print("\n   Type 'quit' to exit the program.")
    choice = input("\nYour choice: ")
    print("\n======================================================\n")

    if choice == "1":
      create_recipe()
    elif choice == "2":
      search_by_ingredients()
    elif choice == "3":
      edit_recipe()
    elif choice == "4":
      delete_recipe()
    elif choice == "5":
      view_all_recipes()
    else:
      if choice == "quit":
        print("Bye!\n")
      else:
        print("WARNING... Wrong entry, please try again.")


# ===============
# -- Main code --
# ===============

# Calls the main_menu() function
main_menu()

session.close()
