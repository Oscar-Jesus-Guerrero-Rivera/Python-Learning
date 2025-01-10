"""
List Division
Write a function called divide_list() that takes a list 
and a number as input. The function returns a new list 
that contains all the elements of the original list except 
they have been divided by the second input.

divided_list = divide_list([6, 8, 10], 2)
print(divided_list) # [3.0, 4.0, 5.0]

Make sure you're appending the raw float values. 
Don't round or cast the numbers to integers.
"""

def list_division(list,n):
    new_list = []
    for x in list:
        new_list.append(x / n)
    return new_list

my_list = list([5,6,7,8,9,10])


print(list_division(my_list, 2))