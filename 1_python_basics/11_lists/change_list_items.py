# To change the value of a specific item, refer to the index number.
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist[1] = "blackcurrant"
print(thislist)
# To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values.
# Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon".
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print(thislist)
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
# If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly.
# Change the second value by replacing it with two new values.
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
# If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly.
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist[1:3] = ["watermelon"]
print(thislist)

print()
# Insert Items
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.
# Insert "watermelon" as the third item.
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist.insert(2, "watermelon")
print(thislist)