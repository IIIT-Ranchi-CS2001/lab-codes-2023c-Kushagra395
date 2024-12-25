#  Define a function my_
# zip() that can form a list of tuples by iterating the
# following customer details:-
# ‘customer Name, customer ID , shopping points’
# and based on the keyword parameter ‘strct’: If strct = True, zipping shall be done
# only if all lists are of equal length. If strct = False, zipping can be done by taking
# the minimum length of the iterable.
def my_zip(*args, strct=True):
    min_len = min(map(len, args)) if strct else len(args[0])
    return [tuple(arg[i] for arg in args) for i in range(min_len)]

names = ["Tom", "Jerry", "Spike"]
ids = [101, 102, 103]
points = [30, 40, 50]
result = my_zip(names, ids, points, strct=True)
print(result)
