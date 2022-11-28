class ShoppingList(object):
  def __init__(self, list_name):
    shopping_list = []
    self.list_name = list_name
    self.shopping_list = shopping_list

  # add_item(self, item): adds an item to self.shopping_list, only if the item isn’t already there.
  def add_item(self, item):
    self.item = item
    # print(self.shopping_list)
    if (item in self.shopping_list):
      print("Item already in the list")
    else:
      self.shopping_list.append(item)
      print("Item added to the list")


  # remove_item(self, item): removes an item from self.shopping_list
  def remove_item(self, item):
    self.item = item
    # print(self.shopping_list)
    if (item in self.shopping_list):
      self.shopping_list.remove(self.item)
      print("Item removed from the list")
    else:
      print("Item not in the list")

  # Prints the contents of self.shopping_list
  def view_list(self):
    print(self.shopping_list)
    print("Items in the shopping list " + self.list_name + ": ")
    print("----------------------------------------------------")
    for item in self.shopping_list:
      print("- " + item)


# Main section of the script
# Initialize a new list
pet_store_list = ShoppingList("Pet Store Shopping List")

# Add the following items to the list using the add_item() method: dog food, frisbee, bowl, collars, flea collars.
pet_store_list.add_item("dog food")
pet_store_list.add_item("frisbee")
pet_store_list.add_item("bowl")
pet_store_list.add_item("collars")
pet_store_list.add_item("flea collars")

# Remove flea collars using the remove_item() method.
pet_store_list.remove_item("flea collars")

# Try adding frisbee again using the add_item() method.
pet_store_list.add_item("frisbee")

# Display the entire shopping list through the view_list() method.
pet_store_list.view_list()
