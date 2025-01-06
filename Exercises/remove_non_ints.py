"""
Complete the remove_nonints() function that takes a list and returns a new list with all the non-integer types removed.

remove_nonints(['1', 1, '3', '400', 4, 500])
"""

def remove_nonints(list):
    int_list = []
    for x in list:
        if type(x) == int:
            int_list.append(x)
        else:
            pass    
    return int_list

print(str(remove_nonints(['1', 1, '3', '400', 4, 500])))

