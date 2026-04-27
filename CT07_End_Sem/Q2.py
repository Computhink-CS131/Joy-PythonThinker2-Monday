num_list = [2944, -5490, 2357, -2619, 1177, 451, -8299, 2533, 4682, -6040, 0]
def is_even(num):
    for num in num_list:
        if num % 2 ==  0:
            return True
        else:
            return False
is_even(num_list)
for num in num_list:
    if is_even(num):
        print(str(num) + " is an even number.")
    else:
        print(str(num) + " is an odd number.")