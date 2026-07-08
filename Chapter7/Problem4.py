# Write a program to find whether a given number is prime or not.

inputTheNo = int(input("Enter a number: "))
for i in range(2, inputTheNo):
    if(inputTheNo%i==0):
        print("Not a prime number")
        break
else:
    print("Prime number")