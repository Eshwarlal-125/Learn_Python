# Write a program to find the sum of first n natural numbers 
# using while loop.

inputTheNo = int(input("Enter a number: "))

sum = 0
i = 0
while(i<=inputTheNo):
    sum += i
    i += 1
print("Sum: ",sum)