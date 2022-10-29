# Python Sets

# Set
'''
    Sets are used to store multiple items in a single variable.
    A set is a collection which is unordered, unchangeable*, and unindexed.
    Sets are written with curly brackets.

    * Note: Set items are unchangeable, but you can remove items and add new items.
'''
thisset = {"apple", "banana", "cherry"}
print(thisset)

print('----------------------------------------------------------------')
# Set Items
    # Set items are unordered, unchangeable, and do not allow duplicate values.

# Unordered
'''
    Unordered means that the items in a set do not have a defined order.
    Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
    Once a set is created, you cannot change its items, but you can remove items and add new items.
'''

# Duplicates Not Allowed
    # Sets cannot have two items with the same value.

# Duplicate values will be ignored.
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

print('----------------------------------------------------------------')
# Get the Length of a Set
    # To determine how many items a set has, use the len() function.
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

print('----------------------------------------------------------------')
# Set Items - Data Types
    # Set items can be of any data type.
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

    # A set can contain different data types.
set1 = {"abc", 34, True, 40, "male"}
print(set1)

print('----------------------------------------------------------------')
# type()
    # From Python's perspective, sets are defined as objects with the data type 'set'.
myset = {"apple", "banana", "cherry"}
print(type(myset))

print('----------------------------------------------------------------')
# The set() Constructor
    # It is also possible to use the set() constructor to make a set.
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

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