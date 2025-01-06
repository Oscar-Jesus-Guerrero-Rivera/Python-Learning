""" Tuples """

# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable.
# Allow duplicates.

thistuple = ("apple", "banana", "cherry")

# Tuple constructor

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets

# Access tuple items

print(thistuple[1]) # (Banana)
print(thistuple[-1]) # (Cherry)
print(thistuple[1:2]) # Admits Ranges

# Check if item exists

if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

# Change tuple values

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

# Add items

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y) # Option 1

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y # Option 2

# Remove items

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

# Delete tuple

thistuple = ("apple", "banana", "cherry")
del thistuple

# Unpack a tuple

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

# Option 2

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, *tropic, red) = fruits # Python will assign values to the variable until the number of values left matches the number of variables left.
print(green)
print(tropic)
print(red)

# Looping through a tuple

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

# Or

for i in range(len(thistuple)):
  print(thistuple[i])

# Or 

i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

# Join tuples

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2

# Multiply tuples

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

# Tuple methods

"""
Method	Description
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
"""