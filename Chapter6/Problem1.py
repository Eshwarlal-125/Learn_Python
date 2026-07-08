# Write a program to find the greatest of four numbers 
# entered by the user.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
num4 = int(input("Enter the fourth number: "))

if(num1 > num2 and num1 > num3 and num1 > num4):
    print("First number is the greatest")
elif(num2>num1 and num2>num3 and num2>num4):
    print("Second number is the greatest")
elif(num3>num1 and num3>num2 and num3>num4):
    print("Third number is the greatest")
else:
    print("Fourth number is the greatest")

