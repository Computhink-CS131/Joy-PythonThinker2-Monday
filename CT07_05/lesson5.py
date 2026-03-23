# # Lesson 5 - List Variables II

# ## Recap 1: Favourite Food List
# **Recap 1a**:
# Create a list of 5 food that you like to eat

# fav_food = [
    # "sushi",
    # "chasoba",
    # "ham",
    # "chawamushi",
    # "miso soup"
# ]
# print(fav_food)

# **Recap 1b**:
# You no longer like to eat the 3rd item on your list,
# delete it

# fav_food = [
#     "sushi",
#     "chasoba",
#     "ham",
#     "chawamushi",
#     "miso soup"
# ]
# fav_food.pop(2)
# print(fav_food)

# # **Recap 1c**:
# # Add 1 more item into your list

# fav_food = [
#     "sushi",
#     "chasoba",
#     "ham",
#     "chawamushi",
#     "miso soup"
# ]
# fav_food.pop(2)
# fav_food.append("momo ice cream")
# print(fav_food)

# # **Recap 1d**:
# # Write a for loop to say all the food items in your list

# for food in fav_food:
#     print("I like to eat: ")
#     print(food)

## Task 1: List of 100 numbers 
# You are preparing for an upcoming lucky draw session at your
# school. You have been tasked to create a program that will pick
# 100 lucky winners.

# By importing the 'random' library and using 'random.randint()',
# create a program to create 100 random numbers in a list
# 1. Use a loop to add 100 random numbers into your list.
# 2. Each number added range between 1 to 1000

# import random
# lucky_num_list = []
# for i in range(100):
#     lucky_num_list.append(random.randint(1, 1000))
# print(lucky_num_list)

## Task 2: List of 100 unique numbers
# The program you have created from the previous task will
# sometimes generate duplicate numbers. Modify your program so
# that the 100 numbers generated are all unique.

# Modify your program from the previous task to create 100 random
# unique numbers in a list.
# 1. Use a loop to add 100 random numbers into your list.
# 2. Each number added range between 1 to 1000
# 3. Ensure that all the numbers are unique
# 4. Print the list of 100 unique numbers created

# Hint: Use a while loop to check if the number already exists in
# the loop

# import random
# lucky_num_list = []
# for i in range(100):
#     lucky_num_list.append(random.randint(1, 1000))
# print(lucky_num_list)
# while len(lucky_num_list) < 100:
#     random_num = random.randint(1, 1000)
#     if random_num not in lucky_num_list:
#         lucky_num_list.append(random_num)
# print(lucky_num_list)
# print(len(lucky_num_list))

# numbers = lucky_num_list
# total_sum = sum(numbers)
# max_num = max(numbers)
# min_num = min(numbers)
# length = len(numbers)
# print(total_sum/length)
# numbers.index(100)

# numbers =[1,2,3,4,5]
# sum = sum(numbers)
# length = len(numbers)
# max_num = max(numbers)
# min_num = min(numbers)

## Task 3: Score Taker
# Imagine the list that you have created in Task 2 represent the
# score of a 100 students.

# Find the maximum, minimum and average from the list.

# 1. Using the 'max()' function, find the maximum score.
# 2. Using the 'min()' function, find the minimum score.
# 3. Using the 'sum()' and 'len()' function, calculate the
#    average score.

## Task 4: Who is the tallest?
# Task: You are given 2 lists, 
# **namelist** contains a list of students in your class
# **heightlist** contains a list of the corresponding student's
#                height

# 1. Determine who is the tallest in class, and what is his/ her
#    name
# 2. Determine who is the shortest in class, and what is his/ her
#    name

# Sample Data (Copy + paste the below code):
# namelist = ["JiJi", "Kobi", "Sunny", "Lily", "AiLing", "Setsuko",
#             "Koko", "Akiro", "Hisaishi", "JiWoo"
#             ]
# heightlist = [160, 165, 158, 170, 162, 168, 159, 172, 164, 166]

# Hint:
# use .index("value of something in the list") to find the index
# of an item

# namelist = ["JiJi", "Kobi", "Sunny", "Lily", "JiYeo", "Setsuko","Koko", "Akiro", "Hisaishi", "JiWoo"]
# heightlist = [126, 125, 127, 118, 123, 119, 123, 121, 129, 126]
# max_height = max(heightlist)
# min_height = min(heightlist)
# max_height_index = heightlist.index(max_height)
# min_height_index = heightlist.index(min_height)
# print("Tallest person is " + namelist[max_height_index])
# print("Shortest person is " + namelist[min_height_index])

## Task 5: Pokemon, I choose you!
# Task: You are given 2 lists,
# **pokemons** contains a list of pokemons
# **powers** contains a list of the corresponding pokemon's
#            powers

# 1. Choose 2 random pokemons from the list
# 2. Compare the powers of the 2 pokemons
# 3. Calculate who is the winner of the fight between these 2
#    pokemons
#    (pokemon with the higher power will always win)

import random

poke = [
    "Shinx", "Staravia", "Houndoom", "Onix",
    "Ponyta", "Geodude", "Psyduck", "Machoke", "Lucairo",
    "Luxray", "Startly", "Budew", "Golbat", "Prinplup",
    "Medetite", "Staraptor", "Gyarados", "Bidoof", "Piplup",
    "Luxio"
]

powers = [
    85, 135, 49, 48, 35,
    45, 52, 101, 119, 140,
    85, 65, 83, 130, 79,
    150, 125, 65, 110, 124
]
poke1 = random.choice(poke)
poke2 = random.choice(poke)
poke1_ind = poke.index(poke1)
poke2_ind = poke.index(poke2)
poke1_power = powers[poke1_ind]
poke2_power = powers[poke2_ind]

print(poke1 + " and " + poke2 + " are fighting!")
if poke1_power == poke2_power:
    print("You are TIED!!!")
elif poke1_power > poke2_power:
    print(poke1 + " wins!")
else:
    print(poke2 + " wins!")

# Hint: import the random library and use random.choice(listname)
