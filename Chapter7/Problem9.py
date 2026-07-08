''' Write a program to print the following star pattern.
* * *
* * for n = 3
* * *
'''
n = 3
for i in range(1,4):
    if i == 2:
        print("* "*(n-1))
    else:
        print("* "*n)