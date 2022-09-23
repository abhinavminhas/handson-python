# Python supports the usual logical conditions from mathematics:
'''
    Equals: a == b
    Not Equals: a != b
    Less than: a < b
    Less than or equal to: a <= b
    Greater than: a > b
    Greater than or equal to: a >= b
    These conditions can be used in several ways, most commonly in "if statements" and loops.
'''
# An "if statement" is written by using the if keyword.
a = 33
b = 200
if b > a:
    print("b is greater than a")

print()
# Elif
# The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".
a = 33
b = 33
if b > a:
  print("b is greater than a")
if b == a:
    print("a and b are equal")

print()
# The else keyword catches anything which isn't caught by the preceding conditions.
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

print()
# You can also have an else without the elif.
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("a is greater than b")

print()
# Short Hand If
# If you have only one statement to execute, you can put it on the same line as the if statement.
if a > b: print("a is greater than b")

print()
# Short Hand If ... Else
# If you have only one statement to execute, one for if, and one for else, you can put it all on the same line.
a = 2
b = 330
print("A") if a > b else print("B")

print()
# You can also have multiple else statements on the same line.
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

print()
# And
# The and keyword is a logical operator, and is used to combine conditional statements.
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

print()
# The or keyword is a logical operator, and is used to combine conditional statements.
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

print()
# Nested If
# You can have if statements inside if statements, this is called nested if statements.
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# The pass Statement
# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
a = 33
b = 200

if b > a:
    pass