# -------------------------------
# STAGE 1 — Function (No Return)
# -------------------------------

# Task 1A:
# Create a function called say_hello that prints:
# "Hello pilot!"
# def say_hello():
    # print("Hello pilot!")


# Task 1B:
# Call the function 3 times
# for i in range(3):
    # say_hello()

# Task 1C (Challenge):
# Create a function called countdown that prints:# 3# 2# 1# Go!
# def countdown():
    # print("3!")
    # print("2!")
    # print("1!")
    # print("Go!")
# countdown()

# -------------------------------
# STAGE 2 — Function with Parameters
# -------------------------------

# Task 2A:
# Create a function greet(name)
# It should print: Hello <name>
# def greet(name):
    # print("Hello " + name + " !")


# Task 2B:
# Call the function with:
# "Alex"
# "Sam"
# greet("Alex")
# greet("Sam")


# Task 2C (Challenge):
# Create a function shoot(player)
# It should print: <player> fires a laser!
# def shoot(player):
    # print(player  + " fires a lazer!")
# shoot("the_lazer_penguin")


# -------------------------------
# STAGE 3 — Function with Return
# -------------------------------

# Task 3A:
# Create a function add_score(score)
# It should return score + 10
# def add_score(score):
    # return score + 10



# Task 3B:
# Call the function with 50
# Store the result in a variable and print it
# end_with_score_50 = add_score(50)
# print(end_with_score_50)

# Task 3C (Challenge):
# Create a function double(x)
# It should return x * 2
def double(x):
    return x * 2
penguin = 11121806
result = double(penguin)
print(result)

# -------------------------------
# STAGE 4 — Calling Function in a Loop
# -------------------------------

# Task 4A:
# Create a function spawn_enemy()
# It should print: Enemy spawned!
def spawn_enemy():
    print("Enemy spawned! Send more penguins to defeat them!")


# Task 4B:
# Use a for loop to call the function 5 times
for i in range(5):
    spawn_enemy()
print("ATTACK! BUY MORE POTIONS TO HEAL! BUY A REVIVE IN CASE!")
print("ERROR. TOO MANY OPPOSING CATS.")


# Task 4C (Challenge):
# Modify spawn_enemy to take a parameter num
# It should print: Enemy <num> spawned!
# Use a loop to spawn 3 enemies with numbers
def spawn_enemy_ultra_alert(num):
    print(f"{num} enemies spawned! Too many enemies! Predicted death in approximately 5 minutes.")
for i in range(1, 4):
    spawn_enemy_ultra_alert(736882*i)

# -------------------------------
# STAGE 5 — Function Inside Function
# -------------------------------

# Task 5A:
# Create two functions:
# move() → prints "Player moves"
# attack() → prints "Player attacks"
def move():
    print("PeNgU1ns_aRe_cuTe moves!")
    print("Uh oh. PeNgU1ns_aRe_cuTe attacks! Your health drains from 1000 health 283 health.")
move()
# Task 5B:
# Create a function take_turn()
# It should call move() and attack()



# Task 5C:
# Call take_turn()



# Task 5D (Challenge):
# Create:
# calculate_damage() → returns 10
# attack() → calls calculate_damage and prints:
# "Dealt <damage> damage!"