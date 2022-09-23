# Python Inheritance
'''
    Inheritance allows us to define a class that inherits all the methods and properties from another class.

    Parent class is the class being inherited from, also called base class.
    Child class is the class that inherits from another class, also called derived class.
'''

# Create a Parent Class
# Any class can be a parent class, so the syntax is the same as creating any other class.
class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        print("My name is " + self.firstname + " " + self.lastname)

x = Person("John", "Doe")
x.printname()

print()
# Create a Child Class
# To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class.
class Student(Person):
    pass

# Note: Use the pass keyword when you do not want to add any other properties or methods to the class.

# Now the Student class has the same properties and methods as the Person class.
# Example - Use the Student class to create an object, and then execute the printname method.
x = Student("Mike", "Olsen")
x.printname()

print()
# Add the __init__() Function
'''
    So far we have created a child class that inherits the properties and methods from its parent.
    We want to add the __init__() function to the child class (instead of the pass keyword).
'''
class Student(Person):
    def __init__(self, firstname, lastname):
        Person.__init__(firstname, lastname)

# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
# Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function.

class Student(Person):
    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname)

# By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.

# Example - Add a property called graduationyear to the Student class.
class Student(Person):
    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname)
        self.graduationyear = 2019

# In the example below, the year 2019 should be a variable, and passed into the Student class when creating student objects. To do so, add another parameter in the __init__() function.
# Example - Add a year parameter, and pass the correct year when creating objects.
class Student(Person):
    def __init__(self, firstname, lastname, year):
        super().__init__(firstname, lastname)
        self.graduationyear = year

x = Student("Mike", "Olsen", 2019)

# Add Methods
# Example - Add a method called welcome to the Student class.
class Student(Person):
    def __init__(self, firstname, lastname, year):
        super().__init__(firstname, lastname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()