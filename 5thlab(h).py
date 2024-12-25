# Sort the list of tuples constructed above with and without sorted function.
# Sorting with sorted()
sorted_with_sorted = sorted(tuples_with_zip, key=lambda x: x[2], reverse=True)
print("Sorted tuples (with sorted()):", sorted_with_sorted)

# Sorting without sorted()
def custom_sort(data):
    for i in range(len(data)):
        for j in range(len(data) - i - 1):
            if data[j][2] < data[j + 1][2]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

sorted_without_sorted = custom_sort(tuples_without_zip)
print("Sorted tuples (without sorted()):", sorted_without_sorted)
