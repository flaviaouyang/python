# Check if any of the items in a list are True:
my_list = [False, True, False]
x = any(my_list)
print(x)

# The any() function returns True if any item in an iterable are true, otherwise it returns False.
# If the iterable object is empty, the any() function will return False.

# Check if all items in a list are True:
my_list = [True, True, True]
x = all(my_list)

# The all() function returns True if all items in an iterable are true, otherwise it returns False.
# If the iterable object is empty, the all() function also returns True.
