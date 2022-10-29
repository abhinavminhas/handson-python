# Python Tuples

# Tuple
'''
    Tuples are used to store multiple items in a single variable.
    A tuple is a collection which is ordered and unchangeable.
    Tuples are written with round brackets.
'''
thistuple = ("apple", "banana", "cherry")
print(thistuple)

print('----------------------------------------------------------------')
# Tuple Items
'''
    Tuple items are ordered, unchangeable, and allow duplicate values.
    Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
'''

# Ordered
    # When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

# Unchangeable
    # Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

# Allow Duplicates
    # Tuples allow duplicate value.
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

print('----------------------------------------------------------------')
# Tuple Length
    # To determine how many items a tuple has, use the len() function.
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

print('----------------------------------------------------------------')
# Create Tuple With One Item
    # To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
thistuple = ("apple",)
print(type(thistuple))

    # NOT a tuple
thistuple = ("apple")
print(type(thistuple))

print('----------------------------------------------------------------')
# Tuple Items - Data Types
    # Tuple items can be of any data type.
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(tuple1)
print(tuple2)
print(tuple3)

    # A tuple can contain different data types.
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)

print('----------------------------------------------------------------')
# type()
    # From Python's perspective, tuples are defined as objects with the data type 'tuple'.
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

print('----------------------------------------------------------------')
# The tuple() Constructor
    # It is also possible to use the tuple() constructor to make a tuple.
thistuple = tuple(("apple", "banana", "cherry"))
print(type(thistuple))

# Python Collections (Arrays)
'''
There are four collection data types in the Python programming language:
    1. List is a collection which is ordered and changeable. Allows duplicate members.
    2. Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    3. Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
    4. Dictionary is a collection which is ordered** and changeable. No duplicate members.

    * Set items are unchangeable, but you can remove and/or add items whenever you like.
    ** As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
'''