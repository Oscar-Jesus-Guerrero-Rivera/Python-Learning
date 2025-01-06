""" Data types """

# Variables

x = 4       # x is of type int
x = "Sally" # x is now of type str

# Casting

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# Get variable type

x = 5
y = "John"
print(type(x))
print(type(y))

# Case sensitive

a = 4
A = "Sally"  #A will not overwrite a

""" 
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
"""

# Assign multiple variables

x, y, z = "Orange", "Banana", "Cherry"

x = y = z = "Orange"

# Unpack collections

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits # x = apple, y = banana, z = cherry

# Print multiple variables
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# //////////////////////////////////////////////////////////////////////////////////////////////////

# Operators


# //////////////////////////////////////////////////////////////////////////////////////////////////

# Data Types

x = "Hello World"	                            # str	
x = 20	                                        # int	
x = 20.5	                                    # float	
x = 1j	                                        # complex	
x = ["apple", "banana", "cherry"]	            # list	
x = ("apple", "banana", "cherry")	            # tuple	
x = range(6)	                                # range	
x = {"name" : "John", "age" : 36}	            # dict	
x = {"apple", "banana", "cherry"}	            # set	
x = frozenset({"apple", "banana", "cherry"})	# frozenset	
x = True	                                    # bool	
x = b"Hello"	                                # bytes	
x = bytearray(5)	                            # bytearray	
x = memoryview(bytes(5))	                    # memoryview	
x = None	                                    # NoneType

# Specifying data types

x = str("Hello World")	                        # str	
x = int(20)	                                    # int	
x = float(20.5)	                                # float	
x = complex(1j)	                                # complex	
x = list(("apple", "banana", "cherry"))	        # list	
x = tuple(("apple", "banana", "cherry"))	    # tuple	
x = range(6)	                                # range	
x = dict(name="John", age=36)	                # dict	
x = set(("apple", "banana", "cherry"))	        # set	
x = frozenset(("apple", "banana", "cherry"))	# frozenset	
x = bool(5)	                                    # bool	
x = bytes(5)	                                # bytes	
x = bytearray(5)	                            # bytearray	
x = memoryview(bytes(5))	                    # memoryview

# str: Represents a sequence of characters
# int: Represents whole numbers without a decimal point
# float: Represents numbers with a decimal point
# complex: Represents a complex number with a real and an imaginary part
# list: Represents an ordered, mutable collection of elements
# tuple: Represents an ordered, immutable collection of elements
# range: Represents a sequence of numbers, typically used in loops
# dict: Represents key-value pairs
# set: Represents an unordered collection of unique elements
# frozenset: Represents an immutable version of a set
# bool: Represents a truth value: True or False
# bytes: Represents immutable sequences of bytes
# bytearray: Represents a mutable sequence of bytes
# memoryview: Provides a view object that exposes an array's internal data without copying it
# NoneType: Represents the absence of a value
