""" 
Write a function called number_sum(n) that adds up all the numbers from 1 to n. For example:

number_sum(5) -> 1+2+3+4+5 -> 15

number_sum(3) -> 1+2+3 -> 6
"""
# Detect user input

try:
    number = 0
    while number <= 0:
       number = int(input("Enter a natural number: "))
    else:
       pass
except:
    print ("An unexpected error ocurred")

# Using recursion

def number_sum(n):
    if (n > 0):
        sum = n + number_sum(n-1)
    else:
        sum = 0
    return sum

print ("The result with recursion is: " + str(number_sum(number)))

# Using for loop

def number_sum2(n):
    sum = 0
    for x in range(n+1):
        sum += x
    return sum

print ("The result with for loop is: " + str(number_sum2(number)))

# Using while loop

def number_sum3(n):
    sum = 0
    while n >= 1:
        sum +=n
        n -= 1
    return sum

print ("The result with while loop is: " + str(number_sum3(number)))

# Using math

def number_sum4(n):
    return n*(n+1)//2

print ("The result with math is: " + str(number_sum4(number)))

# Using comprenhension list

def number_sum5(n):
    return sum([i for i in range(1, n + 1)])

print ("The result with comprenhension list is: " + str(number_sum5(number)))

# Using generative expression

def number_sum6(n):
    return sum(i for i in range(1, n + 1))

print ("The result with generative expression is: " + str(number_sum6(number)))
