# Write a python function to print multiplication table of a given number
def multiplicationTable(num):
    for i in range(1,11):
        print(num,"x",i,"=",num*i)

multiplicationTable(5)