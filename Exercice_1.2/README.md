# Python Task 2

- recipes.py is a simple script that allows to create recipes and add them to an all_recipies variable.
- When called, this script also print out the list of all recipes.

- Data structure selection:
  This app will need some sort of sequence of recipes. For such a sequence we may use either list data type or tuple. We can imagine that the sequence of recipes may need to be extended by the user over time. Also we may want to give the possibility to sort the element of the list. Although tuple main be quicker, due to the fact that tuples are immutable, tuples don’t seem to be the right choice and list datatype would be best in this case to store the recipes. When it comes to each recipe, as each of them includes various properties (name, cooking_time and ingredients), we would need to use a dictionary data type where name would be a string, cooking_time would be an integer and ingredients would be a list (we prefer to use a list instead of a tuple as it brings flexibility in case we want to re-order this list in particular).

- Screenshots:
  Refer to the various folders

- Learning Journal: Answers to questions
