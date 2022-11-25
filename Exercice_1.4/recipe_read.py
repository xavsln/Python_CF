import pickle

my_recipes_file = open("all_recipes_list_and_ingredients.bin", "rb")

recipes_data = pickle.load(my_recipes_file)

print(recipes_data)