# Python Booleans
    # Booleans represent one of two values: True or False.

# Boolean Values
'''
    In programming you often need to know if an expression is True or False.
    You can evaluate any expression in Python, and get one of two answers, True or False.
    When you compare two values, the expression is evaluated and Python returns the Boolean answer:
'''
from traceback import print_tb


print(10 > 9)
print(10 == 9)
print(10 < 9)

print('----------------------------------------------------------------')
    # When you run a condition in an if statement, Python returns True or False.
a = 200
b = 33
if b > a:
    print('b is greater than a')
if a > b:
    print('b is not greater than a')

print('----------------------------------------------------------------')
# Evaluate Values and Variables
    # The bool() function allows you to evaluate any value, and give you True or False in return.
print(bool("Hello"))
print(bool(15))

    # Evaluate two variables.
x = "Hello"
y = 15
print(bool(x))
print(bool(y))

print('----------------------------------------------------------------')
# Most Values are True
'''
    Almost any value is evaluated to True if it has some sort of content.
    Any string is True, except empty strings.
    Any number is True, except 0.
    Any list, tuple, set, and dictionary are True, except empty ones.
'''

    # The following will return True.
a = bool("abc")
b = bool(123)
c = bool(["apple", "cherry", "banana"])
print(a)
print(b)
print(c)

print('----------------------------------------------------------------')
# Some Values are False
    # In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", 
    # the number 0, and the value None. And of course the value False evaluates to False.
a = bool(False)
b = bool(None)
c = bool(0)
d = bool("")
e = bool({})
f = bool(())
g = bool([])
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)

print('----------------------------------------------------------------')
    # One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False.
class MyClass:
  def __len__(self):
    return 0

myobj = MyClass()
print(bool(myobj))

print('----------------------------------------------------------------')
# Functions can Return a Boolean
    # You can create functions that returns a Boolean Value.
def myFunction():
    return True

print(myFunction())

print('----------------------------------------------------------------')
    # You can execute code based on the Boolean answer of a function
def myFunction():
    return True

if (myFunction()):
    print("YES!")
else:
    print("NO!")

print('----------------------------------------------------------------')
    # Python also has many built-in functions that return a boolean value, like the isinstance() function, 
    # which can be used to determine if an object is of a certain data type.
x = 200
print(isinstance(x, int))