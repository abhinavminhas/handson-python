# Python - Global Variables

    # Variables that are created outside of a function (as in all of the examples above) are known as global variables.
    # Global variables can be used by everyone, both inside of functions and outside.

x = "awseome"

def myfunc():
    print("Python is " + x)

myfunc()

print()
    # If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function.
    # The global variable with the same name will remain as it was, global and with the original value.
x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)

print()
    # To change the value of a global variable inside a function, refer to the variable by using the global keyword.
x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)