# To add an item to the end of the list, use the append() method.
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist.append("orange")
print(thislist)

print()
# Insert Items
# To insert a list item at a specified index, use the insert() method.
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist.insert(1, "orange")
print(thislist)

print()
# Extend List
# To append elements from another list to the current list, use the extend() method.
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
tropical.extend(thislist)
print(tropical)