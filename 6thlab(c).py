# Write program to define a function my_
# max() to complete the following tasks:
# [Usage of built-in function max() is strictly prohibited]
# ● If a list of integers is passed as the input argument, the function shall return
# maximum value present in the list
# ● If a set is passed, maximum value present in the list
# ● If a tuple is passed, maximum value present in the tuple
def my_max(*container):
    max_val = container[0]
    for val in container:
        if val > max_val:
            max_val = val
    return max_val

# Example
print(my_max(1, 5, 3, 9, 2))
