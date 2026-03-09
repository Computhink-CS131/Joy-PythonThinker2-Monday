
# print("Hello from lesson 6")

## Task 1: A list within a list 

# You are about to graduate and would like to create a database
# to keep all your friend's contact details using a 2d list.

# Sample Code (Copy + Paste the below code):
# contacts = []
# contact1 = ["John", 98453126, "john@gmail.com"]
# contact2 = ["Adam", 93029102, "adam@gmail.com"]
# contact3 = ["Sylvia", 87894032, "sylvia@gmail.com"]

# 1. append contact1, contact2, and contact3 into contacts
# 2. Write a nested loop to loop through each contact and print
#    the details for each contact



# contacts = []
# contact1 = ["Aizah", 99999999, "aizah@gmail.com"]
# contact2 = ["Lloyd", 88888888, "lloyd@gmail.com"]
# contact3 = ["JunWei", 99998888, "junwei@gmail.com"]
# contacts.append(contact1)
# contacts.append(contact2)
# contacts.append(contact3)
# print(contacts)

# for contacts in contacts:
#     for item in contacts:
#         print(item)

## Task 2: Student List
# You have been given a 2d list of students from a class
# consisting each student's name and their gender:

# Sample Code (Copy + Paste the below code):
# students = [
#     ["JiJi", "F"], ["JiWoo", "M"], ["JiYeo", "F"],
#     ["Koko", "M"], ["Vivian", "F"], ["Akiro", "M"],
#     ["Setsuko", "F"], ["Lucas", "M"], ["Mia", "F"],
#     ["Aiden", "M"], ["Isabella", "F"], ["Jackson", "M"],
#     ["Amelia", "F"], ["Logan", "M"], ["Lily", "F"]
# ]
# ### the above is a nested list. Study and discuss it before we
# ### move on.

# 1. Write a for loop to print out the names of each student and
#    the gender beside.
   
#    e.g. Olivia F
#         Noah M

students = [["JiJi", "F"], ["JiWoo", "M"], ["JiYeo", "F"],
["Koko", "M"], ["Vivian", "F"], ["Akiro", "M"],
["Setsuko", "F"], ["Hisaishi", "M"], ["Ashley", "F"],
["Tam", "M"], ["Storm", "F"], ["Oki", "M"],
["Violet", "F"], ["Ethan", "M"], ["Lily", "F"]]

for student in students:
    name, gender = student
    print(name + " " + gender)

## Task 3: Boys and Girls
# Based on the class list given in the previous task, separate
# the class into 2 lists of boys and girls.

# 1. Create 2 more lists called boys and girls.
# 2. Loop through the 'students' list from the previous task
#    a. if the gender is a boy, add the name into the boys list
#    b. if the gender is a girl, add the name into the girls list
# 3. Write a for loop and name all the boys
# 4. Write a for loop and name all the girls
# 5. Print out how many boys and girls there are

students = [["JiJi", "F"], ["JiWoo", "M"], ["JiYeo", "F"],
["Koko", "M"], ["Vivian", "F"], ["Akiro", "M"],
["Setsuko", "F"], ["Hisaishi", "M"], ["Ashley", "F"],
["Tam", "M"], ["Storm", "F"], ["Oki", "M"],
["Violet", "F"], ["Ethan", "M"], ["Lily", "F"]]

boys = []
girls = []
for student in students:
    name, gender = student
    if gender == "F":
        girls.append(name)
    if gender == "M":
        boys.append(name)
for boy in boys:
    print(boy)
for girl in girls:
    print(girl)
boy_length = len(boys)
girl_length = len(girls)
print("There are " + str(boy_length) + " boys ")
print("There are " + str(girl_length) + " girls ")