# Python - Sort Lists

# Sort List Alphanumerically
    # List objects have a sort() method that will sort the list alphanumerically, ascending, by default.
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

    # Sort the list numerically.
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

print('----------------------------------------------------------------')
# Sort Descending
    # To sort descending, use the keyword argument reverse = True.
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)

    # Sort the list numerically.
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist)

print('----------------------------------------------------------------')
# Customize Sort Function
    # You can also customize your own function by using the keyword argument key = function.
    # The function will return a number that will be used to sort the list (the lowest number first).
thislist = [100, 50, 65, 82, 23]
def myfunc(n):
    return abs(n - 50)
thislist.sort(key=myfunc)
print(thislist)

print('----------------------------------------------------------------')
# Case Insensitive Sort
    # By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters.
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()

    # Perform a case-insensitive sort of the list.
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)

print('----------------------------------------------------------------')
# Reverse Order
    # Reverse the order of the list items.
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)