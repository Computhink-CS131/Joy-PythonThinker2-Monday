"""
============================================================
Q2. Food Order System
============================================================
Write a PYTHON program that simulates a restaurant order
system using list and while loop.

Requirements:
- Use a while loop
- Ask: "What would you like to order?"
- Store each order into a list
- Stop when user enters "end"
- After ending, print all orders in numbered format

============================================================
"""

# ============================================================
# Step 1: Initialize variables
# ============================================================
order = []

# ============================================================
# Step 2: Create a loop
# ============================================================
item = input("What would you like to order? ")
while item != "end":
    order.append(item)
    item = input("What would you like to order? ")
if item == "end":

    print("You have ordered these items:" + str (order))
    # print(i)
    # print(order[i])        



        

# ============================================================
# Step 3: Print the final order summary
# ============================================================
# Print the final order in this format:
# You have ordered the following:
# 1. Item1
# 2. Item2
# 3. Item3
# ============================================================

# ============================================================
# Step 1: Initialize variables
# ============================================================



# ============================================================
# Step 2: Create a loop
# ============================================================



# ============================================================
# Step 3: Print the final order summary
# ============================================================
# Print the final order in this format:
# You have ordered the following:
# 1. Item1
# 2. Item2
# 3. Item3
# ============================================================