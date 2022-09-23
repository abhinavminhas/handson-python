# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# syntax => newlist = [expression for item in iterable if condition == True]
# Example:
#   Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
#   Without list comprehension you will have to write a for statement with a conditional test inside:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist1 = [x for x in fruits if "a" in x]
print(newlist1)
# Only accept items that are not "apple"
newlist2 = [x for x in fruits if x != "apple"]
print(newlist2)
# The condition is optional and can be omitted.
# With no if statement
newlist3 = [x for x in fruits]
print(newlist3)

print()
# Iterable
# The iterable can be any iterable object, like a list, tuple, set etc.
# You can use the range() function to create an iterable.
newlist4 = [x for x in range(10)]
print(newlist4)
# Accept only numbers lower than 5.
newlist5 = [x for x in range(10) if x < 5]
print(newlist5)

print()
# Expression
# The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list.
newlist6 = [x.upper() for x in fruits]
print(newlist6)
# You can set the outcome to whatever you like.
newlist7 = ["Hello" for x in fruits]
print(newlist7)
# The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome.
# Return "orange" instead of "banana":
newlist8 = [x if x != "banana" else "orange" for x in fruits]
print(newlist8)