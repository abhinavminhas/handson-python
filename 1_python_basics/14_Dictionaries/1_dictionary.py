# Python Dictionaries

'''
  Dictionaries are used to store data values in key:value pairs.
  A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

  Note: As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# Dictionary Items
'''
  Dictionary items are ordered, changeable, and does not allow duplicates.
  Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

# Ordered or Unordered?
  # As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

print('----------------------------------------------------------------')
# Changeable
  # Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

# Duplicates Not Allowed
  # Dictionaries cannot have two items with the same key.
  # Duplicate values will overwrite existing values.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

print('----------------------------------------------------------------')
# Dictionary Length
  # To determine how many items a dictionary has, use the len() function.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(len(thisdict))

print('----------------------------------------------------------------')
# Dictionary Items - Data Types
  # The values in dictionary items can be of any data type.
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)

print('----------------------------------------------------------------')
# type()
  # From Python's perspective, dictionaries are defined as objects with the data type 'dict'.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))

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