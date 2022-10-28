# Python Variables
    # Variables are containers for storing data values.

# Creating Variables
    # Python has no command for declaring a variable.
    # A variable is created the moment you first assign a value to it.

x = 5
y = "John"
print(x)
print(y)

    # Variables do not need to be declared with any particular type, and can even change type after they have been set.

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

print('----------------------------------------------------------------')
# Casting
    # If you want to specify the data type of a variable, this can be done with casting.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# Get the Type
    # You can get the data type of a variable with the type() function.

a = str("Hello")
b = "Hi"
c = 'Hey'
d = int(4)
e = float(5)
f = 3
g = 5.00

print(type(a))
print(a)

print(type(b))
print(b)

print(type(c))
print(c)

print(type(d))
print(d)

print(type(e))
print(e)

print(type(f))
print(f)

print(type(g))
print(g)

# Single or Double Quotes?
    # String variables can be declared either by using single or double quotes.

x = "John"
# is the same as
x = 'John'

# Case-Sensitive
    # Variable names are case-sensitive.

a = 4
A = "Sally"
#A will not overwrite a