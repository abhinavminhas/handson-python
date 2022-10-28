# Python Variables - Assign Multiple Values

    # Python allows you to assign values to multiple variables in one line.
x, y, z = "Orange", 3, "Cherry"
print(x)
print(y)
print(z)

print('----------------------------------------------------------------')
# One Value to Multiple Variables
    # You can assign the same value to multiple variables in one line.
x = y = z = "Orange"
print(x)
print(y)
print(z)

print('----------------------------------------------------------------')
# Unpack a Collection
    # If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)