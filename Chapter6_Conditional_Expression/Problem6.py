# Write a program to calculate the grade of a student from 
# his marks from the following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 => C
# 50 – 60 => D
# <50 => F

subj1 = int(input("Enter marks for subject 1: "))
subj2 = int(input("Enter marks for subject 2: "))
subj3 = int(input("Enter marks for subject 3: "))
subj4 = int(input("Enter marks for subject 4: "))
subj5 = int(input("Enter marks for subject 5: "))

total_marks = subj1+subj2+subj3+subj4+subj5

total_percent = (total_marks/500)*100
if(total_percent>=90):
    print("Exellent")
elif(total_percent>=80 and total_percent<90):
    print("A")
elif(total_percent>=70 and total_percent<80):
    print("B")
elif(total_percent>=60 and total_percent<70):
    print("C")
elif(total_percent>=50 and total_percent<60):
    print("D")
else: 
    print("F")