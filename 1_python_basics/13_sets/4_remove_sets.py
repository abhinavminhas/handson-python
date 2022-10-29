# Python - Remove Set Items

# Remove Item
    # To remove an item in a set, use the remove(), or the discard() method.
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
    # Note: If the item to remove does not exist, remove() will raise an error.
    # Note: If the item to remove does not exist, discard() will NOT raise an error.

print('----------------------------------------------------------------')
'''
    You can also use the pop() method to remove an item, but this method will remove the last item.

     Remember that sets are unordered, so you will not know what item that gets removed.
     The return value of the pop() method is the removed item.
'''
thisset = {"apple", "banana", "cherry"}
thisset.pop()
print(thisset)

print('----------------------------------------------------------------')
    # The clear() method empties the set.
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

print('----------------------------------------------------------------')
    # The del keyword will delete the set completely.
thisset = {"apple", "banana", "cherry"}
del thisset