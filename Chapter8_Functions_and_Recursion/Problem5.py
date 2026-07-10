'''
Write a python function to print first n lines of the following pattern.
***
**
*
'''

def pattern(n):
    for i in reversed(range(1,n+1)):
        for j in range(1,i+1):
            print("*", end="")
        print()

pattern(3)