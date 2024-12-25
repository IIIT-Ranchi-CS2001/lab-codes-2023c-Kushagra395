# Define a function my_
# sort() to sort the list of tuples created using my_
# zip
# function in the last question. The function must have two types of arguments- the
# list that carry the data, the key that determines the argument of sorting:
# [Usage of built-in function sorted() is a punishable offense]
# Key = 0: sorting based on customer name in ascending order
# Key = 1: sorting based on Customer ID
# Key = 2: sorting based on shopping points
def my_sort(data, key=0):
    for i in range(len(data)):
        for j in range(len(data) - i - 1):
            if data[j][key] > data[j + 1][key]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

data = [("Tom", 101, 30), ("Jerry", 102, 40), ("Spike", 103, 50)]
sorted_data = my_sort(data, key=2)
print(sorted_data)
