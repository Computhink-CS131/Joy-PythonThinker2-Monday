# print("Hello from lesson 7")



# for i in range(0, len(students), size):
    # new_list.append(students[i:i+size])

## Task 4: Splitting a List in Half
# You have been tasked to divide the basket of fruits into
# 2 equal halves. Given a list of even length, split it
# into 2 equal halves.

# fruits = ["Apple", "Banana", "Cherry", "Durian", "Elderberry", "Figs"]

# 1. Find the midpoint of the list.
# 2. Split the list into 2 halves using slicing.
# 3. Print both halves.

# basket = []
# middle_index = len(basket)//2
# first_half = basket[:3] 
# second_half = basket[3:len(basket)]
# second_half = basket[3:]
# print(f"first half = {first_half}")
# print(f"second_half = {second_half}")

## Task 6: Merging Lists Unique Items
# You have been given 2 lists of fruits that contains duplicates.
# Your task is to merge the 2 lists into a new list that contain
# no duplicates.

# list1 = ["Apple", "Banana", "Cherry", "Cherry"]
# list2 = ["Cherry", "Durian", "Durian", "Figs"]

# 1. Create an empty list named 'unique'
# 2. Using 'for' loops, append unique elements into 'unique'
# 3. Print the unique elements

# unique = []

#check the fruit in list1 not in unique
# if true, we append the fruit to unique

# for fruit in list1:
#     if fruit not in unique:
#         unique.append(fruit)
# for fruit in list2:
#     if fruit not in unique:
#         unique.append(fruit)
# print(unique)
# ---------------------------------------------------------------

# ## Task 7: Merging Lists with Conditions
# You have been given the index number of 2 groups of students.
# However, only students with even index number is allowed
# to come into the room. Create a Python script that will
# merge the 2 lists, including only the elements that are
# even from both.

# list1 = [1, 2, 3, 4]
# list2 = [5, 6, 7, 8]

# Create an empty list, ‘even’​

# Merge the lists using the ‘+’ operator into a list named ‘merged’​

# Using ‘for’ loops and ‘if’ condition, check if each item in the merged list is an
# even number and add them into the ‘even’ list​

# Print the even numbers

# even = []
# for num in list1 + list2:
    # if num %2 == 0:
        # even.append()
# print(even)

## Task 8: Nested List Splitting
# You are given a nested list of 3 groups of students that
# are each seated in a pair. However, you want to unpack
# the nested lists in order to have a list of all students.

nested_list = [[1, 2], [3, 4], [5, 6]]

# 1. Use a loop or list comprehension to flatten the list.
# 2. Print the flattened list.

list3 = []
for list1 in nested_list:
    for item in list1:
        list3.append(item)
# ---------------------------------------------------------------

# ## Task 9: Partitioning a List into Smaller Lists
# You have been tasked to divide a class of 9 students
# into groups of 3.

# Given a list and a size, split the list into multiple
# sub-lists where each sub-list is of the given size.

students = [1, 2, 3, 4, 5, 6, 7, 8, 9] # 123 456 789 0 3 6
size = 3
new_list = []

# 1. Use a loop to create sub-lists of the specified size.
# 2. Print the sub-lists.

# len(students)%3 == (ans)
# print("Each group has " + str(ans) + " students.")



print(new_list)
