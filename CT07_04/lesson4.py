# Task 1: List of planets
# **Task: Create a list of 8 planets in the solar system**

# **Task 1a**:
# Create a list of 8 planets in the solar system.
# (Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune)

# planets = [
#     "Mecury",
#     "Venus",
#     "Earth",
#     "Mars",
#     "Jupiter",
#     "Saturn",
#     "Uranus",
#     "Neptune"
# ]
# print(planets)

# **Task 1b**:
# You have conquered Mars, **rename** Mars to a name of
# your liking

# planets = [
#     "Mecury",
#     "Venus",
#     "Earth",
#     "Mars",
#     "Jupiter",
#     "Saturn",
#     "Uranus",
#     "Neptune"
# ]
# planets[3] = "Penguin Planet"
# print(planets)

# **Task 1c**:
# 1. You have decided Pluto is a planet again, **add** Pluto
#    into the list

# planets = [
#     "Mecury",
#     "Venus",
#     "Earth",
#     "Penguin Planet",
#     "Jupiter",
#     "Saturn",
#     "Uranus",
#     "Neptune"
# ]
# planets.insert(8, "Pluto")
# print(planets)

# 2. You created an artificial planet between Earth and
#    Mars called "Penguin Universe". **Insert** the planet in
#    correctly into the list.

# planets = [
#     "Mecury",
#     "Venus",
#     "Earth",
#     "Penguin Planet",
#     "Jupiter",
#     "Saturn",
#     "Uranus",
#     "Neptune",
#     "Pluto"
# ]
# planets.insert(3, "Penguin Universe")
# print(planets)

# **Task 1d**:
# You launched a war againts Jupiter and destroyed it,
# **delete** Jupiter from the list

# planets = [
#     "Mecury",
#     "Venus",
#     "Earth",
#     "Penguin Planet",
#     "Jupiter",
#     "Saturn",
#     "Uranus",
#     "Neptune",
#     "Pluto"
# ]
# planets.pop(4)
# print(planets)

## Task 2: List of planets (part 2)
# Tasks:

# planet = [
#     "Mecury",
#     "Venus",
#     "Earth",
#     "Penguin Planet ( Mars ) ",
#     "Jupiter ( R.I.P ) ",
#     "Saturn",
#     "Uranus",
#     "Penguin Universe",
#     "Neptune"
# ]
# for p in planet:
#     # print(p) should it be if-else or if-elif-else or if
#     if p == "Earth":
#         print("Earth: This is my home:)")
#     elif p == "Penguin Planet ( Mars ) ":
#         print("Penguin Planet ( Mars ) : I conquered this planet ( it was Mars) and renamed it:)")
#     elif p == "Jupiter ( R.I.P ) ":
#         print("Jupiter: I destroyed this planet:)")
#     elif p == "Penguin Universe":
#         print("Penguin Universe: I created this planet:)")
#     else:
#         print(p)
    
# MErucry
# Venus
# Earth: This is my home

# 1. Write a for loop and print out all the names of the
#    planets
# 2. If name == "Earth", print "<planet name> : this is
#    my home"
# 3. If name == "Mars" (or "Penguin Planet"), print
#    "<planet name> : I conquered this"
# 4. If name == "Penguin Universe", print
#    "<planet name> : I created this"
# 5. If name == "Jupiter", print
#    "<planet name> : I destroyed this"



#

# ## Task 4: Restaurant Menu
# **Task 4a**:
# Write a program to create a menu for a new
# restaurant

# 1. Using a while loop, ask the user (the restaurant manager)
#    to input food items
# 2. Add each food item into the menu list
# 3. End the loop when the user types "end"

# menu_list = []
# order = input("What do you want to eat? : ")
# while order != "end":
#     menu_list.append(order)
#     order = input("Anything else? : ")
# # if input == "end":
# print("Here is what you ordered. Enjoy your meal and have a nice day!")
# print(menu_list) 


# **Task 4b**:
# Based on the list created by the restaurant manager, do
# the following:

# 1. Imagine a customer has come in, ask the customer what
#    would they like to eat?
# 2. If the food is in the list, say "Yes we sell that,
#    please have a seat"
# 3. else, say "Sorry, please go next door, bye."

import random
menu = [
    "ebiko",
    "tamago",
    "inari",
    "chawamushi",
    "miso soup",
    "udon",
    "chasoba",
    "wasabi",
    "shoyu",
]
order = input("What do you want to eat? : ")
if order in menu:
    print("You are seated at Table " + str(random.randint(1, 30)) + ". Do take a seat! ")
else:
    print("Sorry, we don't sell it here. ")




