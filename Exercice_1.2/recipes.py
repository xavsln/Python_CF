recipe_1 = {
  'name': 'Tea',
  'cooking_time': 5,
  'ingredients': ['Tea leaves', 'Sugar', 'Water']
}

all_recipes = []

# all_recipes.append(recipe_1)

print("all_recipes: ", all_recipes)

recipe_2 = {
  'name': 'Coffee',
  'cooking_time': 1,
  'ingredients': ['Coffee', 'Sugar', 'Water']
}

recipe_3 = {
  'name': 'Scrambled eggs',
  'cooking_time': 5,
  'ingredients': ['Eggs', 'Cream', 'Butter']
}

recipe_4 = {
  'name': 'Tomatoe soup',
  'cooking_time': 40,
  'ingredients': ['Tomatoes', 'Onions', 'Butter', 'Water']
}

recipe_5 = {
  'name': 'Bread',
  'cooking_time': 25,
  'ingredients': ['White flour', 'Salt', 'Yeast', 'Water']
}

all_recipes.extend((recipe_2, recipe_3, recipe_4, recipe_5))
print("all_recipes: ", all_recipes)