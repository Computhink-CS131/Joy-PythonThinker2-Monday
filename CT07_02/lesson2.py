# # Lesson 2 - Introduction to while loops

# ## Recap 1: For Loop
# **Task: write a separate 'for' loop to print the following
# numbers:**
# 1. from 0 - 20
# 2. from 1 to 30
# 3. from 2 to 24 (in even numbers)

# for i in range(0, 21):
#     print(i)
# for r in range(1, 31):
#     print(r)
# for h in range(2, 25, 2):
#     print(h)

# ---------------------------------------------------------------

# ## Task 1: Introduction to while loop
# **Task: Using a separate 'while' loop, print each of the
# following:**
# 1. from 0 to 20
# 2. from 1 to 30
# 3. from 2 to 24

# counter = 0
# while counter < 21:
#     print(counter)
#     counter += 1

# counter = 1
# while counter < 31:
#     print(counter)
#     counter += 1

# counter = 2
# while counter < 25:
#     print(counter)
#     counter += 1
    
# extra question(s)!

# print 50 to 25

# counter = 50
# while counter > 24:
#     print(counter)
#     counter -= 1

# print 100 to 86 only even number

# counter = 100
# while counter > 85:
#     print(counter)
#     counter -= 2

# ---------------------------------------------------------------

# ## Task 2: while... break
# The **break** keyword will **break** out (exit) the loop.
# When a **break** is encountered, the code in the **else** will
# not be run.

# Using a while loop:
# 1. print the numbers from 1 to 10
# 2. if the number is 5, **break** out of the loop

# counter = 1
# while counter < 10:
#     print(counter) 
#     counter += 1
#     if counter == 5:
#         break

# ---------------------------------------------------------------

# ## Task 3: while... else
# The else condition will run when the loop exits normally
# i.e. when the while condition is no longer true.

# **Task 3a**: Using a while loop
# 1. print the numbers from 1 to 10
# 2. once count has reached 10, use the else and print "Count
#    has reached 10"

# counter = 1
# while counter < 11:
#     print(counter)
#     counter += 1
# else:
#     print("Count has reached 10.")

# **Task 3b**:
# Now, modify your 'while' loop such that:
# 1. If the number is 5, **break** out of the loop
# 2. Ensure your code has an else

# Observe if the code in the **else** runs.

# counter = 1
# while counter < 11:
#     print(counter)
#     counter += 1
#     if counter == 5:
#         break
#     else:
#         print("Happy New Year!!!!!")

# ---------------------------------------------------------------

# ## Task 4: Ordering Pizzas with while loop
# **Task: Using what you have learned above, code a program to
# take a customer's order for pizza.
# Declare a variable called _topping_.**

# Using a while loop:
# 1. Ask the user to enter a choice of topping
# 2. For each topping entered, concatenate to the 'topping'
#    variable
# 3. exit the while loop if the user enters "end"
# 4. On program end, print out the toppings that the customer
#    has chosen.
# print("Enter your choice of toppings (add a comma at the end). Type 'end' to submit orders.")

# final_topping = " "
# pizza_topping = input("Enter your choice of toppings (or 'end' to submit orders). ")
# while pizza_topping != "end":
#     final_topping += pizza_topping + " "
#     print(final_topping)
#     pizza_topping = input("Enter your choice of toppings (or 'end' to submit orders). ")
# print(final_topping)    

# ---------------------------------------------------------------

# ## Task 5: General Knowledge Quiz
# **Task: Create a program to quiz users on their general
# knowledge**

# Using the while loop, ask 3 general knowledge questions
# 1. Using input ask the question
# 2. While answer is not correct, repeat the question.
# 3. Move on to the next question when the answer is correct

# final_answer = " "
answer = " "
while answer != "9":
    answer = input(" How many brains does an octopus have? : ")
print("Correct!")    

answer = " "
while answer != "a snail":
    answer = input(" What animal has the most teeth? : ")
print("Correct!")    

answer = " "
while answer != "a giraffe":
    answer = input(" What animal has the highest blood pressure? : ")
print("Correct!")

# for reference, another way to do
# while True: 
#     answer = input(" What animal has the highest blood pressure? : ")
#     if answer == "a giraffe":
#         break
# print("Correct!")
print(" You are a science fun-facts star! You rock:) ")