""" Dictionaries """

# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates
# Dictionaries cannot have two items with the same key:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

print(thisdict["brand"]) # Prints the brand value of the dictionary

# Dictionary length

print(len(thisdict))

# The values in dictionary items can be of any data type

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

# Constructor

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

# Access

x = thisdict["model"] # Get the value of the "model" key:
x = thisdict.get("model") # Option 2
x = thisdict.keys() # will return a list of all the keys in the dictionary.

# Add a new item to the original dictionary

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change

# Get all values

x = thisdict.values()

# Make a change in the original dictionary

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

# Get items (tuples)

x = thisdict.items()

# Check if key exists

if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

# Update
thisdict.update({"year": 2020})

# Remove items

# Pop removes the item with the specified key name

thisdict.pop("model")

# Pop item removes the last inserted item
thisdict.popitem()

# You can also use del to delete an item or the whole dict

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

# Clear empties the dictionary

thisdict.clear()

# Loop through a dictionary

for x in thisdict:
  print(x) # Print all key names in the dictionary, one by one:

# Print all values in the dictionary, one by one:

for x in thisdict:
  print(thisdict[x])

# You can also use the values() method to return values of a dictionary:

for x in thisdict.values():
  print(x)

# You can use the keys() method to return the keys of a dictionary:

for x in thisdict.keys():
  print(x)

# Loop through both keys and values, by using the items() method:

for x, y in thisdict.items():
  print(x, y)

# Copy a dictionary

mydict = thisdict.copy() # Option 1
mydict = dict(thisdict) # Option 2

# Nested dictionaries

# Create a dictionary that contain three dictionaries:

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# Create three dictionaries, then create one dictionary that will contain the other three dictionaries:

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily["child2"]["name"])

# Loop through the keys and values of all nested dictionaries:

for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])

# Dictionary methods

"""
Method	    Description
clear()	    Removes all the elements from the dictionary
copy()	    Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	    Returns the value of the specified key
items()	    Returns a list containing a tuple for each key value pair
keys()	    Returns a list containing the dictionary's keys
pop()	    Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
"""