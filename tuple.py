
def sum_list(lst):
    x = 0
    for num in lst:
        x += num
    return x

def count_element(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count

def custom_index(lst, element):
    for i, item in enumerate(lst):
        if item == element:
            return i
    raise ValueError(f"{element} is not in list")

my_list = [1, 2, 3, 4, 3, 5, 3]

# Using sum_list
print("Sum:", sum_list(my_list))

# Using count_element
print("Count of 3:", count_element(my_list, 3))

# Using custom_index
print("Index of 4:", custom_index(my_list, 4))









