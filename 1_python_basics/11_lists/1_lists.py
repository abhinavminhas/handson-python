# Python Lists
'''
    Lists are used to store multiple items in a single variable.
    Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
    Lists are created using square brackets.
'''
# Create a list
thislist = ["apple", "banana", "cherry"]
print(thislist)

print('----------------------------------------------------------------')
    # To determine how many items a list has, use the len() function.
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

print('----------------------------------------------------------------')
    # From Python's perspective, lists are defined as objects with the data type 'list'.
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

print('----------------------------------------------------------------')
    # It is also possible to use the list() constructor when creating a new list.
thislist = list(("apple", "banana", "cherry"))
print(thislist)

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