import mymodule

mymodule.greeting("Jonathan")

a = mymodule.person1["age"]
print(a)

# Naming a Module
# You can name the module file whatever you like, but it must have the file extension .py

# Re-naming a Module
# You can create an alias when you import a module, by using the as keyword.

import mymodule as mx

x = mx.person1["age"]
print(a)

# Built-in Modules
# There are several built-in modules in Python, which you can import whenever you like.
import platform

platform.system()
print(x)

# Using the dir() Function
# There is a built-in function to list all the function names (or variable names) in a module. The dir() function.
import platform

x = dir(platform)
print(x)

print()
# Import From Module
# You can choose to import only parts from a module, by using the from keyword.
from mymodule import greeting
from mymodule import person1

greeting("Jonathan")
print(person1)