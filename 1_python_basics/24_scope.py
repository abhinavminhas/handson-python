# Python Scope
  # A variable is only available from inside the region it is created. This is called scope.

# Local Scope
  # A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
def myfunc():
    x = 300
    print(x)

myfunc()

print('----------------------------------------------------------------')
# Function Inside Function
  # As explained in the example above, the variable x is not available outside the function, but it is available for any function inside the function.
def myfunc():
  x = 400
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

print('----------------------------------------------------------------')
# Global Scope
  # A variable created in the main body of the Python code is a global variable and belongs to the global scope.
  # Global variables are available from within any scope, global and local.
x = 500

def myfunc():
  print(x)

myfunc()
print(x)

print('----------------------------------------------------------------')
# Naming Variables
  # If you operate with the same variable name inside and outside of a function, 
  # Python will treat them as two separate variables, one available in the global scope (outside the function) and one available in the local scope (inside the function).
x = 600

def myfunc():
  x = 700
  print(x)

myfunc()
print(x)

print('----------------------------------------------------------------')
# Global Keyword
  # If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
  # The global keyword makes the variable global.
def myfunc():
  global x
  x = 800
myfunc()
print(x)

print('----------------------------------------------------------------')
  # Also, use the global keyword if you want to make a change to a global variable inside a function.
x = 900
def myfunc():
  global x
  x = 1000
myfunc()
print(x)