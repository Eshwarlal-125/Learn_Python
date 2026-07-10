# Write a program using functions to find greatest of three numbers.

def findGreatestNumber(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return "First Number is Greatest"
    elif num2>=num1 and num2>=num3:
        return "Second Number is greatest"
    else:
        return "Third Number is Greatest"
    
print(findGreatestNumber(12,12,4))