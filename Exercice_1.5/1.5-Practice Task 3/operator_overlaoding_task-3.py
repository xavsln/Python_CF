class Height(object):
  def __init__(self, feet, inches):
    self.feet = feet
    self.inches = inches

  def __str__(self):
    output = str(self.feet) + " feet, " + str(self.inches) + " inches"
    return output

  def __add__(self, other):
    # Converting both objects' heights into inches
    height_A_inches = self.feet * 12 + self.inches
    height_B_inches = other.feet * 12 + other.inches

    # Adding them up
    total_height_inches = height_A_inches + height_B_inches

    # Getting the output in feet
    output_feet = total_height_inches // 12

    # Getting the output in inches
    output_inches = total_height_inches - (output_feet * 12)

    # Returning the final output as a new Height object
    return Height(output_feet, output_inches)

  def __sub__(self, other):
    # Converting both objects' heights into inches
    height_C_inches = self.feet * 12 + self.inches
    height_D_inches = other.feet * 12 + other.inches

    # Substracting them up
    total_height_inches = height_D_inches + height_C_inches

    # Getting the output in feet
    output_feet = total_height_inches // 12

    # Getting the output in inches
    output_inches = total_height_inches - (output_feet * 12)

    # Returning the final output as a new Height object
    return Height(output_feet, output_inches)

  def __lt__(self, other):
    height_inches_A = self.feet * 12 + self.inches
    height_inches_B = other.feet * 12 + other.inches
    return height_inches_A < height_inches_B

  def __le__(self, other):
    height_inches_A = self.feet * 12 + self.inches
    height_inches_B = other.feet * 12 + other.inches
    return height_inches_A <= height_inches_B

  def __eq__(self, other):
    height_inches_A = self.feet * 12 + self.inches
    height_inches_B = other.feet * 12 + other.inches
    return height_inches_A == height_inches_B

  def __gt__(self, other):
    height_inches_A = self.feet * 12 + self.inches
    height_inches_B = other.feet * 12 + other.inches
    return height_inches_A > height_inches_B

  def __ge__(self, other):
    height_inches_A = self.feet * 12 + self.inches
    height_inches_B = other.feet * 12 + other.inches
    return height_inches_A >= height_inches_B

  def __ne__(self, other):
    height_inches_A = self.feet * 12 + self.inches
    height_inches_B = other.feet * 12 + other.inches
    return height_inches_A != height_inches_B

person_A_height = Height(5, 10)
person_B_height = Height(4, 10)
height_sum = person_A_height + person_B_height

print("Total height (after height sum):", height_sum)

person_C_height = Height(3, 9)
person_D_height = Height(5, 10)
height_sub = person_D_height - person_C_height

print("Total height (after height sub):", height_sub)

# comparisons
print(Height(4, 5) < Height(4, 6))
print(Height(4, 5) <= Height(4, 5))
print(Height(5, 10) == Height(5, 10))

print(Height(4, 6) > Height(4, 5))
print(Height(4, 5) >= Height(4, 5))
print(Height(5, 9) != Height(5, 10))