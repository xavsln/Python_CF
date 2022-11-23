a_number = input("Enter the 1st number: ")
b_number = input("Enter the 2nd number: ")
operator_selection = input("Enter + if you want to add the 2nd number to the 1st number. Enter - if you want to substract the 2nd number from the 1st number: ")

a = int(a_number)
b = int(b_number)


if operator_selection == "+":
  result = "The sum of the 2 provided numbers is: " + str(a + b)

elif operator_selection == "-":
  result = "The substraction of the 2 numbers is: " + str(a - b)

else:
  result = "Could not do the operation, please try again."
  # print("Oops, I don't think I have that.")


print(result)

