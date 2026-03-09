# ## Task 1: Study Timer
# **Task: Write a program that acts as a study timer**
# 1. The user must input how many minutes they plan to study
# 2. Use a while loop to count down the minutes
# 3. Display "Good job!" once the timer is up

# Hint: you will need the time.sleep(). However this function
# only takes in seconds.
# You will need to write a conversion algorithm to change
# minutes to seconds

# f"{} "
# import time

# time_min = int(input(" How long do you want to study for? : "))         
# while True:
#     if time_min == 0:
#         break
#     print(f"{time_min} minutes left ")
#     time.sleep(60)
#     time_min -= 1
# print(" RINGGG!!! Hope you enjoyed your learning! ")

# ## Task 3: Multiplication Quiz
# **Task: Ms Tan, your math teacher knows that you are a
# programming whiz,
# she has asked you to help code a multiplication quiz for
# the class to practice.**

# Here are her requirements:
# 1. Students have to answer 15 questions in total
# 2. Students have 3 lives (chances). i.e. they can get the
#    question wrong 3 times.
# 3. The questions will be in this format: "What is 3 x 19? ". 
x
# 5. If the student answers correctly, move on to the next
#    question
# 6. If the student answers wrongly, minus 1 life, and ask
#     the question again.
# 7. If the student has no more lives, exit and print
#     "GO AND SEE MS TAN FOR REMEDIAL"

import random

no_of_qns = 15
no_of_lives = 3

for i in range(no_of_qns):
    num1 = random.randint(2, 21)
    num2 = random.randint(2, 21)
    correct_ans = num1 * num2
    answer = 0

    while answer != correct_ans:
        