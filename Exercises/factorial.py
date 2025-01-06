"""
Complete the factorial() function. It should calculate the factorial of a number. A factorial of a number is the product of all positive integers less than or equal to that number.

For example:

4! = 4 * 3 * 2 * 1 = 24
"""

def factorial(num):
    if (num > 1):
        sum = num * factorial(num-1)
    else:
        sum = 1
    return sum

print (factorial(1))