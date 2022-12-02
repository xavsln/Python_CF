import mysql.connector

conn = mysql.connector.connect(host='localhost', user='cf-python', passwd='password')

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")

cursor.execute("USE task_database")

# Creates a table Recipes
cursor.execute("CREATE TABLE IF NOT EXISTS Recipes (\
id INT PRIMARY KEY AUTO_INCREMENT, \
name VARCHAR(50), \
ingredients VARCHAR(255), \
cooking_time INT, \
difficulty VARCHAR(20) \
)")

# ====================================
# Main Menu - main_menu() function
# ====================================

def main_menu(conn, cursor):
  # Loops until the user decides to type "quit"
  choice = ""
  while(choice != "quit"):
    print("\n======================================================")
    print("\nMain Menu:")
    print("-------------")
    print("Pick a choice:")
    print("   1. Create a new recipe")
    print("   2. Search for a recipe by ingredient")
    print("   3. Update an existing recipe")
    print("   4. Delete a recipe")
    print("   5. View all recipes")
    print("\n   Type 'quit' to exit the program.")
    choice = input("\nYour choice: ")
    print("\n======================================================\n")

    if choice == "1":
      create_recipe(conn, cursor)
    elif choice == "2":
      search_recipe(conn, cursor)
    elif choice == "3":
      update_recipe(conn, cursor)
    elif choice == "4":
      delete_recipe(conn, cursor)
    elif choice == "5":
      view_all_recipes(conn, cursor)

# ====================================
# Main Menu - create_recipe() function
# ====================================
# Function below allows the user to input a new recipe data (name, cooking time, ingredients) and also automatically determines a difficulty level based on cooking time and number of ingredients
def create_recipe(conn, cursor):
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

  # Call calculate_difficulty() that calculates the difficulty of the recipe by taking in cooking_time and ingredients as arguments, and returning one of the following strings: Easy, Medium, Intermediate, or Hard
  difficulty = calc_difficulty(cooking_time, recipe_ingredients)

  # Converts recipe_ingredients into comma-separated strings as MySQL doesn't fully support arrays
  recipe_ingredients_str = ", ".join(recipe_ingredients)

  # adds the recipe to the Recipes table
  sql = 'INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)'
  val = (name, recipe_ingredients_str, cooking_time , difficulty)

  cursor.execute(sql, val)

  # Commits changes made to the Recipes table
  conn.commit()
  print("Recipe saved into the database.")

# calculate_difficulty() calculates the difficulty of the recipe by taking in cooking_time and ingredients as arguments, and returning one of the following strings: Easy, Medium, Intermediate, or Hard
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


# ====================================
# Main Menu - search_recipe() function
# ====================================
def search_recipe(conn, cursor):
  all_ingredients = []

  # Stores the entire list of ingredients available into results
  cursor.execute("SELECT ingredients FROM Recipes")
  results = cursor.fetchall()

  # Note: possible upgrade, in case there is no recipe in the Recipes table, send a message (use try / except / else)
  # print("Results for search ingredients: ", results)

  # Iterates through the results list and for each recipe ingredients tuple
  for recipe_ingredients_list in results:
    # Iterate through recipe ingredients tuple
    for recipe_ingredients in recipe_ingredients_list:
      # split each recipe ingredients tuple
      recipe_ingredient_split = recipe_ingredients.split(", ")
      all_ingredients.extend(recipe_ingredient_split)

  # print("all_ingredients after the loop: ", all_ingredients)

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
    ingredient_searched_nber = input("\nEnter the number corresponding to the ingredient you want to select from the above list: ")

    ingredient_searched_index = int(ingredient_searched_nber) - 1

    ingredient_searched = all_ingredients_list[ingredient_searched_index][1]

    print("\nYou selected the ingredient: ", ingredient_searched)

  except:
    print("An unexpected error occurred. Make sure to select a number from the list.")

  else:
    # Searches for rows in the table that contain search_ingredient within the ingredients column
    print("\nThe recipe(s) below include(s) the selected ingredient: ")
    print("-------------------------------------------------------")

    cursor.execute("SELECT * FROM Recipes WHERE ingredients LIKE %s", ('%' + ingredient_searched + '%', ))

    results_recipes_with_ingredient = cursor.fetchall()

    # Displays the data from each recipe found
    for row in results_recipes_with_ingredient:
      print("\nID: ", row[0])
      print("name: ", row[1])
      print("ingredients: ", row[2])
      print("cooking_time: ", row[3])
      print("difficulty: ", row[4])


# ====================================
# Main Menu - update_recipe() function
# ====================================
def update_recipe(conn, cursor):
  # Display every recipe to the user to allow him to update the one he wants
  view_all_recipes(conn, cursor)

  # Asks the user to input the ID of the recipe he wants to update
  recipe_id_for_update = int((input("\nEnter the ID of the recipe you want to update: ")))

  # Asks the user to input which column he wants to update among name, cooking_time and ingredients
  column_for_update = str(input("\nEnter the data you want to update among name, cooking time and ingredients: (select 'name' or 'cooking_time' or 'ingredients'): "))

  # Asks the user to input the new value
  updated_value = (input("\nEnter the new value for the recipe: "))
  print("Choice: ", updated_value)

  if column_for_update == "name":
    cursor.execute("UPDATE Recipes SET name = %s WHERE id = %s", (updated_value, recipe_id_for_update))
    print("Modification done.")

  elif column_for_update == "cooking_time":
    cursor.execute("UPDATE Recipes SET cooking_time = %s WHERE id = %s", (updated_value, recipe_id_for_update))
    # As cooking_time was changed, it is needed to recalculate the difficulty
    # At first we need to fetch the recipe parameters
    cursor.execute("SELECT * FROM Recipes WHERE id = %s", (recipe_id_for_update, ))
    result_recipe_for_update = cursor.fetchall()

    # print("result_recipe_for_update: ", result_recipe_for_update)

    name = result_recipe_for_update[0][1]
    recipe_ingredients = tuple(result_recipe_for_update[0][2].split(','))
    cooking_time = result_recipe_for_update[0][3]

    updated_difficulty = calc_difficulty(cooking_time, recipe_ingredients)
    print("Updated difficulty: ", updated_difficulty)
    cursor.execute("UPDATE Recipes SET difficulty = %s WHERE id = %s", (updated_difficulty, recipe_id_for_update))
    print("Modification done.")

  elif column_for_update == "ingredients":
    cursor.execute("UPDATE Recipes SET ingredients = %s WHERE id = %s", (updated_value, recipe_id_for_update))
    # As ingredients were changed, it is needed to recalculate the difficulty
    # At first we need to fetch the recipe parameters
    cursor.execute("SELECT * FROM Recipes WHERE id = %s", (recipe_id_for_update, ))
    result_recipe_for_update = cursor.fetchall()

    print("result_recipe_for_update: ", result_recipe_for_update)

    name = result_recipe_for_update[0][1]
    recipe_ingredients = tuple(result_recipe_for_update[0][2].split(','))
    cooking_time = result_recipe_for_update[0][3]
    difficulty = result_recipe_for_update[0][4]

    updated_difficulty = calc_difficulty(cooking_time, recipe_ingredients)
    print("Updated difficulty: ", updated_difficulty)
    cursor.execute("UPDATE Recipes SET difficulty = %s WHERE id = %s", (updated_difficulty, recipe_id_for_update))
    print("Modification done.")

  # Commits changes made to the Recipes table
  conn.commit()

# ====================================
# Main Menu - delete_recipe() function
# ====================================
def delete_recipe(conn, cursor):
  # Display every recipe to the user to allow him to delete the one he wants
  view_all_recipes(conn, cursor)

  # Asks the user to input the ID of the recipe he wants to delete
  recipe_id_for_deletion = (input("\nEnter the ID of the recipe you want to delete: "))

  # Delete the corresponding recipe into result  
  cursor.execute("DELETE FROM Recipes WHERE id = (%s)", (recipe_id_for_deletion, ))

  # Commits changes made to the Recipes table
  conn.commit()
  print("\nRecipe successfully deleted from the database.")


# =======================================
# Main Menu - view_all_recipes() function
# =======================================
def view_all_recipes(conn, cursor):
  print("\nAll recipes can be found below: ")
  print("-------------------------------------------")

  # Stores the entire list of recipes into results
  cursor.execute("SELECT * FROM Recipes")
  results = cursor.fetchall()

  # Displays the data from each recipe found
  for row in results:
    print("\nID: ", row[0])
    print("name: ", row[1])
    print("ingredients: ", row[2])
    print("cooking_time: ", row[3])
    print("difficulty: ", row[4])


# ===============
# -- Main code --
# ===============

# Calls the main_menu() function
main_menu(conn, cursor)
print("Bye!\n")
