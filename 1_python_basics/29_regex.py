# Python RegEx
'''
    A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
    RegEx can be used to check if a string contains the specified search pattern.
'''

# RegEx Module
    # Python has a built-in package called re, which can be used to work with Regular Expressions.

# Import the re module.
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)

# RegEx Functions
'''
    The re module offers a set of functions that allows us to search a string for a match:
        Function    Description
        findall     Returns a list containing all matches
        search      Returns a Match object if there is a match anywhere in the string
        split       Returns a list where the string has been split at each match
        sub         Replaces one or many matches with a string
'''

# Metacharacters
    # Metacharacters are characters with a special meaning.
'''
    Character	Description	                                                                    Example
    []	        A set of characters                                                             "[a-m]"	
    \	        Signals a special sequence (can also be used to escape special characters)	    "\d"	
    .	        Any character (except newline character)	                                    "he..o"	
    ^	        Starts with	                                                                    "^hello"	
    $	        Ends with	                                                                    "planet$"	
    *	        Zero or more occurrences                                                        "he.*o"	
    +	        One or more occurrences                                                         "he.+o"	
    ?	        Zero or one occurrences                                                         "he.?o"	
    {}	        Exactly the specified number of occurrences	                                    "he.{2}o"	
    |	        Either or	                                                                    "falls|stays"	
    ()	        Capture and group
'''

# Sets
    # A set is a set of characters inside a pair of square brackets [] with a special meaning.
'''
    Set             Description
    [arn]           Returns a match where one of the specified characters (a, r, or n) is present	
    [a-n]           Returns a match for any lower case character, alphabetically between a and n	
    [^arn]          Returns a match for any character EXCEPT a, r, and n	
    [0123]          Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
    [0-9]           Returns a match for any digit between 0 and 9	
    [0-5][0-9]      Returns a match for any two-digit numbers from 00 and 59	
    [a-zA-Z]        Returns a match for any character alphabetically between a and z, lower case OR upper case	
    [+]             In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string
'''

print('----------------------------------------------------------------')
# The findall() Function
    # The findall() function returns a list containing all matches.
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

print('----------------------------------------------------------------')
# The list contains the matches in the order they are found.
    # If no matches are found, an empty list is returned.
txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

print('----------------------------------------------------------------')
# The search() Function
    # The search() function searches the string for a match, and returns a Match object if there is a match.
    # If there is more than one match, only the first occurrence of the match will be returned.
txt = "The rain in Spain"
x = re.search("\s", txt)
print(x)
print("The first white-space character is located in position: ", x.start())

print('----------------------------------------------------------------')
    # If no matches are found, the value None is returned.
txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)

print('----------------------------------------------------------------')
# The split() Function
    # The split() function returns a list where the string has been split at each match.
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

print('----------------------------------------------------------------')
    # You can control the number of occurrences by specifying the maxsplit parameter.
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

print('----------------------------------------------------------------')
# The sub() Function
    # The sub() function replaces the matches with the text of your choice.
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

print('----------------------------------------------------------------')
    # You can control the number of replacements by specifying the count parameter.
txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

print('----------------------------------------------------------------')
# Match Object
    # A Match Object is an object containing information about the search and the result.
    # Note: If there is no match, the value None will be returned, instead of the Match Object.
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object

print('----------------------------------------------------------------')
    # The Match object has properties and methods used to retrieve information about the search, and the result:
'''
    .span()     returns a tuple containing the start-, and end positions of the match.
    .string     returns the string passed into the function
    .group()    returns the part of the string where there was a match
'''
    # Print the position (start- and end-position) of the first match occurrence.
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

print('----------------------------------------------------------------')
    # Print the string passed into the function.
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

print('----------------------------------------------------------------')
    # Print the part of the string where there was a match.
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())