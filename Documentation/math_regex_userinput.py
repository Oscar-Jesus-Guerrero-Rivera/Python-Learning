""" Math, RegEx, User Input """

# The min() and max() functions can be used to find the lowest or highest value in an iterable:

x = min(5, 10, 25)
y = max(5, 10, 25)

# The abs() function returns the absolute (positive) value of the specified number:

x = abs(-7.25)

# The pow(x, y) function returns the value of x to the power of y (xy).

x = pow(4, 3)

# Math Module

# math.sqrt() method for example, returns the square root of a number:

import math

x = math.sqrt(64)

print(x)

# math.ceil() method rounds a number upwards to its nearest integer, 
# and the math.floor() method rounds a number downwards to its nearest integer, and returns the result:

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1

# The math.pi constant, returns the value of PI (3.14...):

x = math.pi

# RegEx

# Functions
"""
Function	Description
findall	    Returns a list containing all matches
search	    Returns a Match object if there is a match anywhere in the string
split	    Returns a list where the string has been split at each match
sub	        Replaces one or many matches with a string
"""

# MetaCharacters
"""
Character	Description	                                                                Example	
[]	        A set of characters	"[a-m]"	
\	        Signals a special sequence (can also be used to escape special characters)	"\d"	
.	        Any character (except newline character)	                                "he..o"	
^	        Starts with	                                                                "^hello"	
$	        Ends with	                                                                "planet$"	
*	        Zero or more occurrences	                                                "he.*o"	
+	        One or more occurrences	                                                    "he.+o"	
?	        Zero or one occurrences	                                                    "he.?o"	
{}	        Exactly the specified number of occurrences	                                "he.{2}o"	
|	        Either or	                                                                "falls|stays"	
()	        Capture and group	 
"""

# Special sequences

"""
\A	Returns a match if the specified characters are at the beginning of the string Ex: "\AThe"	

\b	Returns a match where the specified characters are at the beginning or at the end of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string") Ex: r"\bain"
r"ain\b"	

\B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) 
of a word (the "r" in the beginning is making sure that the string is being treated as a 
"raw string") Ex: r"\Bain" r"ain\B"	

\d	Returns a match where the string contains digits (numbers from 0-9)	"\d"	
\D	Returns a match where the string DOES NOT contain digits	"\D"	
\s	Returns a match where the string contains a white space character	"\s"	
\S	Returns a match where the string DOES NOT contain a white space character	"\S"	
\w	Returns a match where the string contains any word characters (characters from a to Z, d
igits from 0-9, and the underscore _ character)	"\w"	
\W	Returns a match where the string DOES NOT contain any word characters	"\W"	
\Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"
"""

# Sets

"""
[arn]	Returns a match where one of the specified characters (a, r, or n) is present	
[a-n]	Returns a match for any lower case character, alphabetically between a and n	
[^arn]	Returns a match for any character EXCEPT a, r, and n	
[0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
[0-9]	Returns a match for any digit between 0 and 9	
[0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	
[a-zA-Z]	Returns a match for any character alphabetically between a and z, lower 
case OR upper case	
[+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a 
match for any + character in the string
"""

# User input

username = input("Enter username:")
print("Username is: " + username)
