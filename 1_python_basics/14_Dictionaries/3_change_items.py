# Python - Change Dictionary Items

# Change Values
  # You can change the value of a specific item by referring to its key name.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)

print('----------------------------------------------------------------')
# Update Dictionary
'''
  The update() method will update the dictionary with the items from the given argument.
  The argument must be a dictionary, or an iterable object with key:value pairs.
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)