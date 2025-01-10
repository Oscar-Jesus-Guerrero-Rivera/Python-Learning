"""
FizzBuzz
Fizzbuzz is a commonly overused little toy-program 
that comes up in entry-level interviews. This is a little test-able spin on it.

Complete the fizzbuzz function that loops over all the numbers 
from start to end (excluding the end value) and adds them to a list it returns. 
If the number is a multiple of 3, instead of appending the number, append "fizz". 
If the number is a multiple of 5, instead append "buzz". 
If it is a multiple of 3 and 5 then instead append "fizzbuzz".

Tip
As always for the range function, the start is inclusive and the end is exclusive. 
Do not include the end value.
"""

def fizzbuzz(start, end):
    list = []
    n = start - 1 
    while n < end:
        n += 1
        if (n % 3 == 0 and n % 5 == 0):
            list.append("fizzbuzz")
            print ("fizzbuzz")
        elif (n % 3 == 0):
            list.append("fizz")
            print("fizz")
        elif (n % 5 == 0):
            list.append("buzz")
            print("buzz")
        else:
            list.append(n)
            print(n)
    return list


print(fizzbuzz(10,20))
