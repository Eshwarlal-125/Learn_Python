# Write a program to find the maximum of the numbers in a list using the reduce function

from functools import reduce
l = [1,2,3,4,5,6,7,8,9]

def greater(a,b):
    if a>b:
        return a
    return b

final = reduce(greater,l)
print(final)