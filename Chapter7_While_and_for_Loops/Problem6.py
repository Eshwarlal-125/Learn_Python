# Write a program to calculate the factorial of a 
# given number using for loop.

inputTheNo = int(input("Enter a number: "))

fact = 1
for i in range(1,inputTheNo+1):
    fact*=i

print("Factorial = ", fact)