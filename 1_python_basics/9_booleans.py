# Booleans represent one of two values: True or False.
print(10 > 9)
print(10 == 9)
print(10 < 9)

print()
# Print a message based on whether the condition is True or False.
a = 200
b = 33
if b > a:
    print('b is greater than a')
if a > b:
    print('b is not greater than a')

print()
# The bool() function allows you to evaluate any value, and give you True or False in return.
print(bool("Hello"))
print(bool(15))