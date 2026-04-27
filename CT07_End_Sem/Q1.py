daily_sales = [1205, 986, 1354, 10535, 15741, 11200, 800, 13056, 952, 1100,
1025, 8574, 14014, 9987, 1238, 1458, 7803, 900, 13674, 14539, 13241, 10886,
7541, 8743, 1482, 11523, 977, 12181, 8903, 1008, 1530]
# days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
# 27, 28, 29, 30, 31]
# for i in range(len(daily_sales)):
# print(max(daily_sales))
# print(min(daily_sales))
# print(str() + " August"+ " has highest sales of $" + str(max(daily_sales)))

"""
============================================================
Q1. August Sales Analysis
============================================================
You are analysing the daily sales of an e-commerce store for August.
The sales for the 31 days are provided in a list.

Program Requirements:
- Use the list:
  daily_sales = [1205, 986, 1354, 10535, 15741, 11200, 800, 
                 13056, 952, 1100, 1025, 8574, 14014, 9987, 
                 1238, 1458, 7803, 900, 13674, 14539, 13241, 
                 10886, 7541, 8743, 1482, 11523, 977, 12181, 
                 8903, 1008, 1530]

- Find the day with the highest sales
- Find the day with the lowest sales
- Calculate the average daily sales

Print the result exactly in this format:
    5 August has highest sales of $15741
    7 August has lowest sales of $800
    Average daily sales for August is $6714.71

Note:
- The first item in the list represents 1 August
- The average must be rounded to 2 decimal places

============================================================
"""

# ============================================================
# Step 1: Create the list
# ============================================================



# ============================================================
# Step 2: Find highest sales
# ============================================================
max_sale = max(daily_sales)
max_index = 0
for i in range(len(daily_sales)):
    if daily_sales[i] == max(daily_sales):
        max_index = i
print("August " + str(max_index + 1) + " has highest sales of $" + str(max_sale) + " .")

# ============================================================
# Step 3: Find lowest sales
# ============================================================
min_sale = min(daily_sales)
min_index = 0
for i in range(len(daily_sales)):
    if daily_sales[i] == min(daily_sales):
        min_index = i
print("August " + str(min_index + 1) + " has lowest sales of $" + str(min_sale) + " .")
# ============================================================
# Step 4: Calculate average sales (round to 2 decimal places)
# ============================================================
total = 0
length = len(daily_sales)
for num in daily_sales:
    total = total + num
average_sale = total/length
average_sale = round(average_sale, 2)
# for i in range(len(daily_sales)):
#     if daily_sales[i] == a(daily_sales):
#         average_sale = i
print("Average daily sales for August is $" + str(average_sale) + " .")

# ============================================================
# Step 5: Print results in correct format
# ============================================================
