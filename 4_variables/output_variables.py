# The Python print() function is often used to output variables.
x = "Python is awesome"
print(x)


x = "Python"
y = "is"
z = "awesome"
print(x, y, z)


x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error.
# The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types.
x = 5
y = "John"
print (x, y)