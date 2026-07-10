# Write a program to print multiplication table of n using 
# for loops in reversed order.

inputTheNo = int(input("Enter a number and get table: "))

for i in reversed(range(1,11)):
    print(inputTheNo,"x",i,"=",inputTheNo*i)