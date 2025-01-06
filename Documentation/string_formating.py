""" Python String Formatting """

"""
F-String was introduced in Python 3.6 and is now the preferred way of formatting strings.

Before Python 3.6, we used the `format()` method.

---

**F-Strings**

An f-string allows you to format selected parts of a string by including an `f` before the string literal.

Example:
"""
txt = f"The price is 49 dollars"
print(txt)

# Placeholders and Modifiers
"""
Placeholders `{}` in an f-string can contain variables, operations, functions, or modifiers to format the value.

Example:
"""
price = 59
txt = f"The price is {price} dollars"
print(txt)

"""
Modifiers can format values within placeholders. For example, `:.2f` formats a number with 2 decimals.

Example:
"""
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

"""
You can also format values directly without storing them in variables.

Example:
"""
txt = f"The price is {95:.2f} dollars"
print(txt)

# Perform Operations in F-Strings
"""
You can perform operations inside placeholders.

Example:
"""
txt = f"The price is {20 * 59} dollars"
print(txt)

"""
Perform math operations on variables:

Example:
"""
price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)

"""
Use `if...else` statements inside placeholders:

Example:
"""
price = 49
txt = f"It is very {'Expensive' if price > 50 else 'Cheap'}"
print(txt)

# Execute Functions in F-Strings
"""
Functions can be executed inside placeholders.

Example:
"""
fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)

"""
Custom functions can also be used:

Example:
"""
def myconverter(x):
    return x * 0.3048

txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)

# More Modifiers
"""
Examples of formatting types:

- Use a comma as a thousand separator:
"""
price = 59000
txt = f"The price is {price:,} dollars"
print(txt)

"""
List of formatting types:

:<   - Left align
:>   - Right align
:^   - Center align
:=   - Place the sign to the leftmost position
:+   - Use a plus sign for positive/negative results
:-   - Use a minus sign for negatives only
:,   - Comma as a thousand separator
:_   - Underscore as a thousand separator
:b   - Binary format
:c   - Unicode character
:d   - Decimal format
:e   - Scientific format (lowercase e)
:E   - Scientific format (uppercase E)
:f   - Fixed point format
:g   - General format
:o   - Octal format
:x   - Hex format (lowercase)
:X   - Hex format (uppercase)
:n   - Number format
:%   - Percentage format
"""

# String `format()`
"""
Before Python 3.6, the `format()` method was used for string formatting.

Example:
"""
price = 49
txt = "The price is {} dollars"
print(txt.format(price))

"""
You can specify parameters inside curly brackets to format values.

Example:
"""
txt = "The price is {:.2f} dollars"
price = 49
print(txt.format(price))

"""
Multiple values can be formatted:

Example:
"""
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

"""
Use index numbers to ensure values are in the correct placeholders:

Example:
"""
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

"""
Named indexes can also be used:

Example:
"""
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname="Ford", model="Mustang"))
