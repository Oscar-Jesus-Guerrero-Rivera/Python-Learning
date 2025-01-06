""" If, Else and Elif, While and For"""

"""
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
These conditions can be used in several ways, most commonly in "if statements" and loops
"""

# Example

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# Short if

if a > b: print("a is greater than b")

# Short if else

print("A") if a > b else print("B")

# One line if else statement, with 3 conditions:

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# if statements cannot be empty, but if you for some reason have an if statement with no content, 
# put in the pass statement to avoid getting an error.

a = 33
b = 200

if b > a:
  pass

# While loop

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# With the continue statement we can stop the current iteration, and continue with the next:

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# while else

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

# For

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

# Range returns a sequence of numbers, starting from 0 by default, 
# and increments by 1 (by default), and ends at a specified number.

for x in range(6):
  print(x)

# For else

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

# Nested loops

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

# For pass

for x in [0, 1, 2]:
  pass