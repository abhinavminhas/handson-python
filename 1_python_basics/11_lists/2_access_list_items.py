# Python - Access List Items

# Access Items
    # List items are indexed and you can access them by referring to the index number.
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

print('----------------------------------------------------------------')
    # Negative indexing means start from the end.
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

print('----------------------------------------------------------------')
    # Print the last item of the list.
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

print('----------------------------------------------------------------')
    # You can specify a range of indexes by specifying where to start and where to end the range.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) # Note: The search will start at index 2 (included) and end at index 5 (not included).

print('----------------------------------------------------------------')
    # This example returns the items from the beginning to, but NOT including, "kiwi".
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

print('----------------------------------------------------------------')
    # By leaving out the end value, the range will go on to the end of the list.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

print('----------------------------------------------------------------')
    # Specify negative indexes if you want to start the search from the end of the list.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

print('----------------------------------------------------------------')
# Check if Item Exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")