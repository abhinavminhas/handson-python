# Python File Open

# Open a File on the Server
    # To open the file, use the built-in open() function.
    # The open() function returns a file object, which has a read() method for reading the content of the file.
f = open("demofile.txt", "r")
print(f.read())

print('----------------------------------------------------------------')
    # If the file is located in a different location, you will have to specify the file path, like this.
'''
    f = open("C:/home/demofile.txt", "r")
    print(f.read())
'''

# Read Only Parts of the File
    # By default the read() method returns the whole text, but you can also specify how many characters you want to return.
f = open("demofile.txt", "r")
print(f.read(5))

print('----------------------------------------------------------------')
# Read Lines
    # You can return one line by using the readline() method.
f = open("demofile.txt", "r")
print(f.readline())

print('----------------------------------------------------------------')
    # By calling readline() two times, you can read the two first lines.
f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())

print('----------------------------------------------------------------')
    # By looping through the lines of the file, you can read the whole file, line by line.
f = open("demofile.txt", "r")

for x in f:
    print(x)

print('----------------------------------------------------------------')
# Close Files
    # It is a good practice to always close the file when you are done with it.
f = open("demofile.txt", "r")
print(f.readline(5))
f.close()