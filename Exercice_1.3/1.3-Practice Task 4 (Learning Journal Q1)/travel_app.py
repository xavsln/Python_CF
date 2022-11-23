# In this Exercise, you learned how to use if-elif-else statements to run different tasks based on conditions that you define. Now practice that skill by writing a script for a simple travel app using an if-elif-else statement for the following situation: 

# ●	The script should ask the user where they want to travel. 
# ●	The user’s input should be checked for 3 different travel destinations that you define. 
# ●	If the user’s input is one of those 3 destinations, the following statement should be printed: “Enjoy your stay in ______!”
# ●	If the user’s input is something other than the defined destinations, the following statement should be printed: “Oops, that destination is not currently available.”


# Defines travel destinations
travel_destinations = ["Lisbon", "Oslo", "Roma"]

# Asks user to enter a destination
user_destination = str(input("Where do you want to travel?: "))

# Creates a flag to check whether there is a match between the destination entered by the user and the destinations in the travel_destinations list
destination_match = False

# Loops through the destination elements available in the travel_destinations list
for destination in travel_destinations:
  # If the destination entered by the user is equal to one of the destination available in the travel_destinations list it will print out "Enjoy your stay in ... !"
  if (user_destination == destination):
    destination_match = True
    print("Enjoy your stay in " + destination + "!")
    # Exit the loop in case there is a match
    break
  else:
    continue

# If at the end of the code after iteration on all the elements of the travel_destinations list there was no match then the destination_match flag will remain False and therefore we can print out "Oops, that destination is not currently available."
if destination_match == False:
  print("Oops, that destination is not currently available.")
  
