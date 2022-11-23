#================================
# CODE PRACTICE 3: LOOPS

# Let’s pause for a moment to recap loops with the help of another optional practice task. Take a look at the following code:

# print(10)
# print(20)
# print(30)
# print(40)
# print(50)
# print("And we're done!")
# To practice what you’ve learned, complete the following steps and take screenshots of your Python shell after each step:

# 1. Rewrite the above code using a for loop.
# 2. Rewrite the code using a while loop.
# 3. Create a sub folder inside your “Exercise 1.3” folder and name it “1.3-Practice Task 3” or something similar. Upload the screenshots you captured for the previous steps in this folder.

#================================


#----------------------------------------------------------
# 1.a. Rewrite the above code using a for loop. - Version 1
#----------------------------------------------------------

print("\nFor Loop:")

for n in range (10,60,10):
  print(n)

print("And we're done!")


#---------------------------------------------
# 2. Rewrite the code using a while loop.
#---------------------------------------------

print("\nWhile Loop:")

n = 10

while n < 60:
  print(n)
  n +=10

print("And we're done!")



