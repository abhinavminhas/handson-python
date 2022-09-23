# Unpacking a Tuple
# When we create a tuple, we normally assign values to it. This is called "packing" a tuple.
# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking".

# Packing a tuple
fruits = ("apple", "banana", "cherry")

# Unpacking a tuple
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
# Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.

print()
# Using Asterisk*
# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list.
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

print()
#If the asterisk is added to another variable name than the last, 
# Python will assign values to the variable until the number of values left matches the number of variables left.
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, *yellow, red) = fruits
print(green)
print(yellow)
print(red)