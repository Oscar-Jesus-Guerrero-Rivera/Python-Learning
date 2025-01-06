""" Lists """

"""
List items are ordered, changeable, and allow duplicate values.

List items are indexed, the first item has index [0], the second item has index [1] etc.

Ordered
When we say that lists are ordered, it means that the items have a defined order, 
and that order will not change.

If you add new items to a list, the new items will be placed at the end of the list.

Note: There are some list methods that will change the order, but in general: 
the order of the items will not change.
"""

thislist = ["apple", "banana", "cherry"]
print(thislist)

# Changeable

# The list is changeable, meaning that we can change, add, and remove items in a list 
# after it has been created.

# Allow duplicates

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# List length

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# List items can be of any data type and contain different data types

# List constructor

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

# List access

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[1]) # Print the second item of the list
print(thislist[-1]) # Print the last item of the list
print(thislist[2:5]) # Return the third, fourth, and fifth item:
print(thislist[:4]) # This example returns the items from the beginning to, but NOT including, "kiwi"
print(thislist[2:]) # This example returns the items from "cherry" to the end
print(thislist[-4:-1])  # This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):
if "apple" in thislist:   # Check if "apple" is present in the list:
  print("Yes, 'apple' is in the fruits list")

# Change list

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist[1] = "blackcurrant" # Change the second item
thislist[1:3] = ["blackcurrant", "watermelon"] # Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon"
# If you insert more or less items than you replace, the new items will be inserted where you specified, and the remaining
# items will move accordingly:
thislist[1:2] = ["blackcurrant", "watermelon"]
thislist[1:3] = ["watermelon"] 

# Insert

thislist.insert(2, "watermelon") # Insert "watermelon" as the third item:

# Add

thislist.append("orange") 

# Extend

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)  # Add the elements of tropical to thislist:

# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# Remove (just the first ocurrence)

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Remove especified index (last index if not especified)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# del also do the same, but can delete the whole list

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist

# Clear the list

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# Loop through list

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)  # Prints every element on the list

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])  # Print all items by referring to their index number

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

# List comprehension
# newlist = [expression for item in iterable if condition == True]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

# Sort lists

# Alphabetically

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"] 
# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters
thislist.sort()
print(thislist)
thislist.sort(reverse = True) # Descending
thislist.sort(key = str.lower) # Case sensitive
thislist.reverse() # Reverse the list regardless of the alphabet

# Numerically

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
thislist.sort(reverse = True) # Descending

# Customized

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

# Copy a list

# You cannot copy a list simply by typing list2 = list1, because: 
# list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy() # Option 1
mylist = list(thislist) # Option 2
mylist = thislist[:] # Option 3
print(mylist)

# Join lists

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2 # Option 1
for x in list2:
  list1.append(x) # Option 2
list1.extend(list2) # Option 3

# List Methods

"""
Method	    Description
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list
"""