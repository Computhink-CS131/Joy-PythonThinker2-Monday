student_indexes = [1042, 1099, 1031, 1120, 1075, 1042, 1108, 1019, 1063, 1099, 1156, 1027, 1084, 1111, 1031, 1143, 1055, 1108, 1070, 1132, 1055, 1168, 1020, 1084, 1175]
# Task​

# Given a list of student index numbers (with duplicates), create a cleaned list where each
# student appears once.​

# Sort the cleaned list in ascending order.​

# Print the final list and also print how many duplicates were removed.​

# Print the count of how many students attended the Math Enrichment Class.

# sort = sorted(student_indexes)
# print(sort)

# unique = []
# duplicates = 0

# for student in student_indexes:
#     if student not in unique:
#         unique.append(student)
#     else:
#         duplicates += 1
# attendance = len(unique)
# print("There are " + str(attendance) + " students that attended the Math Enrichment Class.")
# print("There are " + str(duplicates) + " duplicates that were removed.")
# print("Have a nice day!")

# Task 1a​
# Ask the user to input their first name until it is a valid name. ​
# A valid name only contains alphabets.​
# Keep asking for a name until a valid name is input.​

# Task 1b​
# Ask the user to input their age until it is a valid number. ​
# Keep asking for a name until a valid number is input.​

# Task 1c​
# Ask the user to input a valid username. A valid username must contain
# alphabets and numbers, but not contain special characters​


# first_name = " "
# while not first_name.isalpha():
#     first_name = input("What is your first name? : ")
    
# print("Your first name is " + first_name + ".")

# age = " "
# while not age.isdigit():
#     age = input("What is your age? : ")

# print("Your age is " + age + ".")

# password = " "
# while not password.isalnum() or password.isdigit() or password.isalpha():
    # password = input("Can you key in your password (don't prank me pls) : ")

# print("Your password is " + password + ".")
# print("Please enter our time - travel portal.")

# Task 2a​
# Ask the user to input their phone number until it is valid using
# a while loop.​
# Make sure to check if the input is the correct data type as well!​

# Task 2b​
# Ask the user to a username and check if it is between 5 to 18
# characters long.​

# phonenum = " "
# while not phonenum.isdigit() or len(phonenum) != 8:
#     phonenum = input("What is your phone number? : ")

# print("Your phone number is " + phonenum + ".")
# failed_attempts = 0
# username = input("What is your username (don't prank me pls) ? : ")
# while not username.isalnum() or len(username) <5 or len(username) >18:
#     print("ERROR!")
#     failed_attempts += 1
#     username = input("What is your username (don't prank me pls) ? : ")
 
# print("Your username is " + username + " with a length of " + str(len(username)) + " .")
# print("And you had " + str(failed_attempts) + " failed attempts.")

# # Lesson 8 - Input Validation

# ## Recap 1: List Manipulation
# You have a list of student index numbers who attended the Math Enrichment class. 
# However, some students’ attendance were recorded more than once due to a human error.
# Your task is to clean the list and produce a list of unique Student Indexes

# Given a list of student index numbers (with duplicates), create a cleaned list where each student appears once.
# Sort the cleaned list in ascending order.
# - Print the final list and also print how many duplicates were removed.
# - Print the count of how many students attended the Math Enrichment Class.

# student_indexes = [1042, 1099, 1031, 1120, 1075, 1042, 1108, 1019, 1063, 1099, 1156, 1027, 1084, 1111, 1031, 1143, 1055, 1108, 1070, 1132, 1055, 1168, 1020, 1084, 1175]

# ## Task 1: Data Format Check

# ### Task 1a
# Ask the user to input their first name until it is a valid name. 
# A valid name only contains alphabets.
# Keep asking for a name until a valid name is input.

# ### Task 1b
# Ask the user to input their age until it is a valid number. 
# Keep asking for a name until a valid number is input.

# ### Task 1c
# Ask the user to input a valid username. A valid username must contain alphabets and numbers, but not contain special characters

# ## Task 2: Length Check (using a while loop)

# ### Task 2a
# Ask the user to input their phone number until it is valid using a while loop.
# Make sure to check if the input is the correct data type as well!

# ### Task 2b
# Ask the user to a username and check if it is between 5 to 18 characters long.

# ## Task 3: Range Check (using a while loop)

# ### Task 3a
# Ask the user to input their birth year and check if it is between 1900 and the current year. Keep asking until a correct value is given.
# while True:
#     birthyear = input("What year were you born? (and don't prank me pls): ")
#     if birthyear.isdigit() and int(birthyear) >= 1900 and int(birthyear) <= 2026:
#         break
#     else:
#         print("DIDN'T I TELL YOU NOT TO PRANK ME? NOW I'VE GOT A HEADACHE!")
# print("Your birth year is " + str(birthyear) + " .")
# ### Task 3b
# Ask the user to input their volume setting and check if it is between 0 and 100.
# while True:
    # volume = input("What is your device's volume? (and don't prank me pls): ")
    # if volume.isdigit() and int(volume) >= 0 and int(volume) <= 100:
#         break
#     else:
#         print("DIDN'T I TELL YOU NOT TO PRANK ME? NOW I'VE GOT A HEADACHE!")
# print("Your device's volume is " + str(volume) + " .")
# ## Task 4: Mocking Text Generator
# Create a program that will turn regular sentences into a “SpongeBob Mocking” meme.
# For example, the program will turn “Hello my name is James” into “HeLlO mY nAmE iS jAmEs”
# sentence = input("What is your sentence? : ")
# new_sentence = ""
# for i in range(len(sentence)):
    # if i % 2 == 0:
#         new_sentence = new_sentence + sentence[i].upper()
#     else:
#         new_sentence = new_sentence + sentence[i].lower()
# print(new_sentence)

# sentence = input("What is your sentence? ")
# new_sentence = ""
# is_upper = True
# for char in sentence:
#     if char.isalpha():
#         if is_upper:
#             new_sentence += char.upper()
#         else:
#             new_sentence += char.lower()
#         is_upper = not is_upper
#     else:
#         new_sentence += char
# print(new_sentence)

# 1. Using input(), ask the user for a sentence
# 2. Use loops to iterate through each letter in the sentence
# 3. Alternate between .upper() and .lower() for each letter
# 4. Print the result.
# SINGAPORE
# 012345678
# ## Task 5: Slice String
# word = “SINGAPORE”
# word = "SINGAPORE"
# print(word[:4])
# print(word[3:6])
# print(word[5:])
# print(word[::2])
# Slice the string and print these words:
# a. SING
# b. GAP
# c. PORE
# d. SNAOE

# ## Task 6: Palindrome
# Ask the user for an input and check if it is a palindrome, until the input is ‘end’.
# word = "empeoleon"
# while True:
#     word = input("What is the word? : ")
#     if word.lower() == "end":
#         break
#     if word == word[::-1]:
#         print(word + " is a palindrome!")
#     else:
#         print(word + " is not a palindrome.")

# You can try this list of words:
# - civic, kayak, level, madam, radar, refer, rotator, tenet, racecar, deified, stats, wow

# ## Task 7: Presence and Existence Checks
# You are hosting a Birthday Party and have invited your friends.

# Create a list with your friends’ names
# - e.g. [“Alice”, “Bob”, Carl”, “Dylan”]

# Write a program to ask for the visitor’s name and check if:
# - Name is entered (presence check)
# - Name is in your friend list (existence check)

# Ask for an input again if a name was not entered.
# Accept the visitor if they are in the list, else deny their entry.
# friends = ["Aizah", "Lloyd", "JunWei", "JingHyun", "Mommy"]
# while True:
#     name = input("What is your name? : ")
#     if name == "":
#         continue

#     if name in friends:
#         print("Please enter.")
#         break
#     else:
#         print("WHAT DO YOU THINK YOU'RE DOING, TRYING TO SNEAK IN?")

# ## Task 8: Format Check
# Ask the user to input their NRIC you need to check:
# 1. First and last character are alphabets in upper case
# 2. First letter must be S, T, F, G, or M.
# 3. Have 7 digits between the alphabets
# 4. Be 9 characters long

first_letter = ["S", "T", "F", "G", "M"]
first_last_letter_is_upper = False
first_letter_is_in_list = False
between_is_seven_digit = False
nine_characters = False

while True:
    nric = input("What is your NRIC? : ").strip()

    if nric == "":
        print("Your NRIC cannot be empty or blank.")
        continue

    if len(nric) == 9:
        nine_characters = True
    else:
        print("Your NRIC number must contain 9 characters.")

    if nric[0].isupper() and nric[-1].isupper():
        first_last_letter_is_upper = True
    else:
        print("Your first letter and last letter must be uppercase.")

    if nric[1:8].isdigit():
        between_is_seven_digit = True
    else:
        print("There must be seven digits between your first letter and last letter.")
    
    if nine_characters and first_last_letter_is_upper and first_letter_is_in_list and between_is_seven_digit:
        break
print("Your NRIC number is " + str(nric) + " . Have a nice day.")
    



# ## Task 9: Password Validation
# A website requires all passwords to
# 1. Be at least 8 characters long
# 2. Contain an upper and lower case
# 3. Contain a number
# 4. No other characters except alphabets or numbers.

# Write a program that will ask the user for a password, and check if the password fits all criteria

# at_least_eight_char = False
# lower_case = False
# upper_case = False
# got_num = False
# is_alnum = False

# print("This is Demon Kitties official website. Please sign in with your DKfanclub account in order to view our videos.")

# while True:
#     DKfanclub = input("What is your DKfancub password? : ").strip()

#     if DKfanclub == "":
#         print("Your DKfanclub password cannot be empty or blank.")
#         continue

#     if len(DKfanclub) >= 8:
#         at_least_eight_char = True
#     else:
#         print("Your DKfanclub password must contain at least 8 characters.")

#     for char in DKfanclub:
#         if char.isupper():
#             upper_case = True
#         if char.islower():
#             lower_case = True
#         if char.isdigit():
#             got_num = True    

#     if DKfanclub.isalnum():
#         is_alnum = True
#     else:
#         print("There should not be any special characters in your DKfanclub password.")
    
#     if is_alnum and got_num and at_least_eight_char and upper_case and lower_case:
#         break
# print("Your DKfanclub password number is " + str(DKfanclub) + " . Enjoy our videos and be cool! 😎 ")

# You may use some of the following passwords to test your program:
# - PassW0rd
# - H3ll0W0r1d
# - BestF00d
# - pa55Me