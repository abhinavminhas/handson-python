# Loop Through a Tuple
# You can loop through the tuple items by using a for loop.
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

print()
# Loop Through the Index Numbers
thistuple = ("apple", "banana", "cherry")
i = 0
for i in range(len(thistuple)):
    print(thistuple[i])
    i += 1

print()
# Using a While Loop
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i += 1