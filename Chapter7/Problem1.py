# Write a program to print multiplication table of a given number 
# using for loop.

inputTheNo = int(input("Enter a number and get table: "))

for i in range(1,11):
    print(inputTheNo, "x" , i , "=" , inputTheNo*i)
