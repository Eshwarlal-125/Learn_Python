# Write a program to accept marks of 6 students
# and display them in a sorted manner

num1 = int(input("Enter marks of student 1: "))
num2 = int(input("Enter marks of student 2: ")) 
num3 = int(input("Enter marks of student 3: "))
num4 = int(input("Enter marks of student 4: "))
num5 = int(input("Enter marks of student 5: "))
num6 = int(input("Enter marks of student 6: "))

list_of_marks = [num1, num2, num3, num4, num5, num6]
list_of_marks.sort()
print(list_of_marks)

'''
list1 = []
for i in range(6):
    number = int(input("Enter Number: "))
    list1.append(number)

list1.sort()
print(list1)"
'''
