# String Methods
    # Python has a set of built-in methods that you can use on strings.

'''
    Method          Description
    capitalize()    Converts the first character to upper case
    casefold()      Converts string into lower case
    center()        Returns a centered string
    count()         Returns the number of times a specified value occurs in a string
    encode()        Returns an encoded version of the string
    endswith()      Returns true if the string ends with the specified value
    expandtabs()    Sets the tab size of the string
    find()          Searches the string for a specified value and returns the position of where it was found
    format()        Formats specified values in a string
    format_map()    Formats specified values in a string
    index()         Searches the string for a specified value and returns the position of where it was found
    isalnum()       Returns True if all characters in the string are alphanumeric
    isalpha()       Returns True if all characters in the string are in the alphabet
    isdecimal()     Returns True if all characters in the string are decimals
    isdigit()       Returns True if all characters in the string are digits
    isidentifier()  Returns True if the string is an identifier
    islower()       Returns True if all characters in the string are lower case
    isnumeric()     Returns True if all characters in the string are numeric
    isprintable()   Returns True if all characters in the string are printable
    isspace()       Returns True if all characters in the string are whitespaces
    istitle()       Returns True if the string follows the rules of a title
    isupper()       Returns True if all characters in the string are upper case
    join()          Joins the elements of an iterable to the end of the string
    ljust()         Returns a left justified version of the string
    lower()         Converts a string into lower case
    lstrip()        Returns a left trim version of the string
    maketrans()     Returns a translation table to be used in translations
    partition()     Returns a tuple where the string is parted into three parts
    replace()       Returns a string where a specified value is replaced with a specified value
    rfind()         Searches the string for a specified value and returns the last position of where it was found
    rindex()        Searches the string for a specified value and returns the last position of where it was found
    rjust()         Returns a right justified version of the string
    rpartition()    Returns a tuple where the string is parted into three parts
    rsplit()        Splits the string at the specified separator, and returns a list
    rstrip()        Returns a right trim version of the string
    split()         Splits the string at the specified separator, and returns a list
    splitlines()    Splits the string at line breaks and returns a list
    startswith()    Returns true if the string starts with the specified value
    strip()         Returns a trimmed version of the string
    swapcase()      Swaps cases, lower case becomes upper case and vice versa
    title()         Converts the first character of each word to upper case
    translate()     Returns a translated string
    upper()         Converts a string into upper case
    zfill()         Fills the string with a specified number of 0 values at the beginning
'''

# capitalize()	Converts the first character to upper case and the rest is lower case.
txt1 = "hello, And Welcome to my World."
txt2 = "python is FUN!"
print(txt1.capitalize())
print(txt2.capitalize())

print('----------------------------------------------------------------')
# casefold()	Converts string into lower case
# This method is similar to the lower() method, 
# but the casefold() method is stronger, more aggressive, meaning that it will convert more characters into lower case, 
# and will find more matches when comparing two strings and both are converted using the casefold() method.
txt = "Hello, And Welcome To My World!"
print(txt.casefold())

print('----------------------------------------------------------------')
# center()	Returns a centered string.
txt = "banana"
x = txt.center(20)
print(x)
# The center() method will center align the string, using a specified character (space is default) as the fill character.
txt = "banana"
print(txt.center(20, 'O'))

print('----------------------------------------------------------------')
# count()	Returns the number of times a specified value occurs in a string.
txt = "I love apples, apple are my favorite fruit"
print(txt.count('apple'))
print(txt.count('apple', 10, 20))

# encode()	Returns an encoded version of the string, using the specified encoding. If no encoding is specified, UTF-8 will be used.
txt = "My name is Ståle"
print(txt.encode())

print('----------------------------------------------------------------')
# endswith()	Returns true if the string ends with the specified value.
txt = "Hello, welcome to my world."
print(txt.endswith('.'))
print(txt.endswith('my world', 5, 11))

print('----------------------------------------------------------------')
# expandtabs()	Sets the tab size of the string. The expandtabs() method sets the tab size to the specified number of whitespaces.
txt = "H\te\tl\tl\to"
print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))


print('----------------------------------------------------------------')
# find()	Searches the string for a specified value and returns the position of where it was found.
# The find() method finds the first occurrence of the specified value.
# The find() method returns -1 if the value is not found.
# The find() method is almost the same as the index() method, the only difference is that the index() method raises an exception if the value is not found.
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)
x = txt.find("e")
print(x)
x = txt.find("e", 5, 10)
print(x)

print('----------------------------------------------------------------')
# format()	Formats specified values in a string.
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John", 36)
txt3 = "My name is {}, I'm {}".format("John", 36)
print(txt1)
print(txt2)
print(txt3)

print('----------------------------------------------------------------')
# index()	Searches the string for a specified value and returns the position of where it was found.
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)
x = txt.index("e")
print(x)
x = txt.index("e", 5, 10)
print(x)

# If the value is not found, the find() method returns -1, but the index() method will raise an exception.
txt = "Hello, welcome to my world."
print(txt.find("q"))
#print(txt.index("q"))

print('----------------------------------------------------------------')
# isalnum()	Returns True if all characters in the string are alphanumeric.
txt = "Company12"
x = txt.isalnum()
print(x)

print('----------------------------------------------------------------')
# isalpha()	Returns True if all characters in the string are in the alphabet.
txt = "CompanyX"
x = txt.isalpha()
print(x)
txt = "Company10"
x = txt.isalpha()
print(x)

print('----------------------------------------------------------------')
# isdecimal()	Returns True if all characters in the string are decimals (0-9).
# This method is used on unicode objects.
a = "\u0030" #unicode for 0
b = "\u0047" #unicode for G
print(a.isdecimal())
print(b.isdecimal())

print('----------------------------------------------------------------')
# isdigit()	Returns True if all characters in the string are digits.
txt = "50800"
x = txt.isdigit()
print(x)

print('----------------------------------------------------------------')
# isidentifier()	Returns True if the string is an identifier.
# A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). 
# A valid identifier cannot start with a number, or contain any spaces.
a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"
print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())

print('----------------------------------------------------------------')
# islower()	Returns True if all characters in the string are lower case.
a = "Hello world!"
b = "hello 123"
c = "mynameisPeter"
print(a.islower())
print(b.islower())
print(c.islower())

print('----------------------------------------------------------------')
# isnumeric()	Returns True if all characters in the string are numeric.
a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for &sup2;
c = "10km2"
d = "-1"
e = "1.5"
print(a.isnumeric())
print(b.isnumeric())
print(c.isnumeric())
print(d.isnumeric())
print(e.isnumeric())