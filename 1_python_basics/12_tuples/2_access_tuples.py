# Python - Access Tuple Items

# Access Tuple Items
    # You can access tuple items by referring to the index number, inside square brackets.
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

print('----------------------------------------------------------------')
# Negative Indexing
    # Negative indexing means start from the end.
    # -1 refers to the last item, -2 refers to the second last item etc.
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

print('----------------------------------------------------------------')
# Range of Indexes
'''
    You can specify a range of indexes by specifying where to start and where to end the range.
    When specifying a range, the return value will be a new tuple with the specified items.
'''
    # Return the third, fourth, and fifth item.
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
    # By leaving out the start value, the range will start at the first item.
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
    # By leaving out the end value, the range will go on to the end of the list.
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])
    # Specify negative indexes if you want to start the search from the end of the tuple.
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

print('----------------------------------------------------------------')
# Check if Item Exists
    # To determine if a specified item is present in a tuple use the in keyword.
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")
