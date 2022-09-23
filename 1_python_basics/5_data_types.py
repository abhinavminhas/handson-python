# Python Data Types

# Built-in Data Types
'''
    In programming, data type is an important concept.
    Variables can store data of different types, and different types can do different things.
    Python has the following data types built-in by default, in these categories:
        Text Type:	    str
        Numeric Types:	int, float, complex
        Sequence Types:	list, tuple, range
        Mapping Type:	dict
        Set Types:	    set, frozenset
        Boolean Type:	bool
        Binary Types:	bytes, bytearray, memoryview
        None Type:	    NoneType
'''

# Getting the Data Type
    # You can get the data type of any object by using the type() function.
x = 5
print(type(x))

print()
# Setting the Data Type
    # In Python, the data type is set when you assign a value to a variable.
x = "Hello World"
x = 20
x = 20.5
x = 1j
x = ["apple", "banana", "cherry"]
x = ("apple", "banana", "cherry")
x = range(6)
x = {"name" : "John", "age" : 36}
x = {"apple", "banana", "cherry"}
x = frozenset({"apple", "banana", "cherry"})
x = True
x = b"Hello"
x = bytearray(5)
x = memoryview(bytes(5))
x = None
print(x)

print()
# Setting the Specific Data Type
    # If you want to specify the data type, you can use the following constructor functions.

x = str("Hello World")
x = int(20)
x = float(20.5)
x = complex(1j)
x = list(("apple", "banana", "cherry"))
x = tuple(("apple", "banana", "cherry"))
x = range(6)
x = dict(name = "John", age = 36)
x = set(("apple", "banana", "cherry"))
x = frozenset(("apple", "banana", "cherry"))
x = bool(5)
x = bytes(5)
x = bytearray(5)
x = memoryview(bytes(5))
print(x)