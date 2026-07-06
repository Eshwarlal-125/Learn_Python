# Write a program to input eight numbers from the user
#  and display all the unique numbers (once).

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
num3 = input("Enter the third number: ")
num4 = input("Enter the fourth number: ")
num5 = input("Enter the fifth number: ")
num6 = input("Enter the sixth number: ")
num7 = input("Enter the seventh number: ")
num8 = input("Enter the eighth number: ")

numbers = set()
numbers.add(num1)
numbers.add(num2)
numbers.add(num3)
numbers.add(num4)
numbers.add(num5)
numbers.add(num6)
numbers.add(num7)
numbers.add(num8)

print("The unique numbers are: ", numbers)