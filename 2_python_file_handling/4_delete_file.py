# Delete a File
# To delete a file, you must import the OS module, and run its os.remove() function.
import os

f = open("file.txt", "x")
f.close()
os.remove("file.txt")

# Check if File exist:
# To avoid getting an error, you might want to check if the file exists before you try to delete it.
if os.path.exists("file.txt"):
    os.remove("file.txt")
else:
    print("The file does not exist")

print()
# To delete an entire folder, use the os.rmdir() method.
if (str(os.path).endswith("myfolder")):
    os.rmdir("myfolder")
else:
    print("The folder does not exist")