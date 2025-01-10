"""
Write a function called find_min() that finds the smallest number in a list

find_min([1, 3, -1, 2]) -> -1

find_min([18, 3, 7, 2]) -> 2
"""

# Get user input and convert it into a list

try:
    user_input = list(map(int, input("Enter numbers separated by space: ").split()))
    print("List:", user_input)
except ValueError:
    print("Error: Please enter only numbers separated by spaces.")

# Function

def find_min(list):
    smallest = int(list[0])
    for x in list:
        if x < smallest:
            smallest = x
        else:
            pass
    print ("The smallest number is: " + str(smallest))
    return smallest

# Calling the function

find_min(user_input)