""" Sets """

# A set is a collection which is unordered, unchangeable*, and unindexed.
# * Note: Set items are unchangeable, but you can remove items and add new items.
# Duplicates not allowed
# True and 1 is considered the same value as well as False and 0

thisset = {"apple", "banana", "cherry"}
print(thisset)

# Get length

print(len(thisset))

# Constructor

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets

# Access

for x in thisset:
  print(x) # Loop through

print("banana" in thisset) # Check if

# Add items

thisset.add("orange")

# Add sets

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

# Add any iterable

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

# Remove item

thisset.remove("banana") # If the item doesnt exists it will raise an error

# Discard

thisset.discard("banana") # If the item doesnt exists it will not raise an error

# Remove random item

x = thisset.pop() 

# Clear the set

thisset.clear()

# Delete the set

del thisset

# Loop through sets

for x in thisset:
  print(x)

# Join sets

# Union

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)

myset = set1 | set2 # I dont get this one

# Join sets with other iterables

x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)

# Update

# inserts all items from one set into another. 
# The update() changes the original set, and does not return a new set.

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)

# Intersection

# will return a new set, that only contains the items that are present in both sets.
# You can use the & operator instead of the intersection() method, and you will get the same result.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)

# intersection update
# will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

# Difference

# will return a new set that will contain only the items from
# the first set that are not present in the other set.
# You can use the - operator instead of the difference() method, and you will get the same result.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

# Difference update

#  will also keep the items from the first set that are not in 
# the other set, but it will change the original set instead of returning a new set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

# Symmetric difference
# will keep only the elements that are NOT present in both sets.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

# Symmetric difference uptdate

# will also keep all but the duplicates, but it will change 
# the original set instead of returning a new set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

# Set Methods

"""
Method	             Shortcut	        Description
add()	 	                            Adds an element to the set
clear()	 	                            Removes all the elements from the set
copy()	 	                            Returns a copy of the set
difference()	        -	            Returns a set containing the difference between two or more sets
difference_update()	    -=	            Removes the items in this set that are also included in another, specified set
discard()	 	                        Remove the specified item
intersection()	        &	            Returns a set, that is the intersection of two other sets
intersection_update()	&=	            Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	 	                    Returns whether two sets have a intersection or not
issubset()	            <=	            Returns whether another set contains this set or not
 	                    <	            Returns whether all items in this set is present in other, specified set(s)
issuperset()	        >=	            Returns whether this set contains another set or not
 	                    >	            Returns whether all items in other, specified set(s) is present in this set
pop()	 	                            Removes an element from the set
remove()	 	                        Removes the specified element
symmetric_difference()	^	            Returns a set with the symmetric differences of two sets
symmetric_difference_update()	^=	    Inserts the symmetric differences from this set and another
union()	                |	            Return a set containing the union of sets
update()	            |=	            Update the set with the union of this set and others
"""